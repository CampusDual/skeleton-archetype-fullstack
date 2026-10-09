import json
import os
import re
import time

from dotenv import load_dotenv
from openai import BadRequestError, OpenAI
import jwt
from jwt.exceptions import InvalidKeyError
import requests

load_dotenv()

# ==========================================================
# GitHub Models
# ==========================================================

MODELS_TOKEN = os.getenv("MODELS_TOKEN")

MODEL_NAME = os.getenv("MODELS_MODEL", "gpt-4o-mini")

# ==========================================================
# GitHub App
# ==========================================================

APP_ID = os.getenv("APP_ID")
INSTALLATION_ID = os.getenv("INSTALLATION_ID")

OWNER = os.getenv("OWNER")
REPO = os.getenv("REPO")

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
PRIVATE_KEY_PATH = os.getenv(
    "PRIVATE_KEY_PATH",
    os.path.join(ROOT_DIR, "github-app.pem")
)


def validate_required_env():

    required = {
        "MODELS_TOKEN": MODELS_TOKEN,
        "APP_ID": APP_ID,
        "INSTALLATION_ID": INSTALLATION_ID,
        "OWNER": OWNER,
        "REPO": REPO,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise RuntimeError(
            "Faltan variables de entorno requeridas: "
            + ", ".join(missing)
            + ". Revisa tu archivo .env."
        )

# ==========================================================
# GitHub App Authentication
# ==========================================================

def create_jwt():

    if not os.path.exists(PRIVATE_KEY_PATH):
        raise RuntimeError(
            f"No se encontró la clave privada de GitHub App en: {PRIVATE_KEY_PATH}. "
            "Configura PRIVATE_KEY_PATH en .env o coloca github-app.pem en la raíz del repo."
        )

    with open(PRIVATE_KEY_PATH, "r") as f:
        private_key = f.read()

    now = int(time.time())

    payload = {
        "iat": now - 60,
        "exp": now + 600,
        "iss": APP_ID
    }

    try:
        return jwt.encode(
            payload,
            private_key,
            algorithm="RS256"
        )
    except InvalidKeyError as exc:
        raise RuntimeError(
            "La clave privada no tiene formato PEM valido. "
            "Revisa APP_PRIVATE_KEY en GitHub Secrets: debe contener el contenido completo "
            "(BEGIN/END) y conservar los saltos de linea."
        ) from exc


def get_installation_token():

    jwt_token = create_jwt()

    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json"
    }

    url = (
        "https://api.github.com/app/installations/"
        f"{INSTALLATION_ID}/access_tokens"
    )

    response = requests.post(
        url,
        headers=headers
    )

    response.raise_for_status()

    return response.json()["token"]


# ==========================================================
# GitHub API Helpers
# ==========================================================

def github_headers(token):

    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


def list_existing_issues(token):

    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{REPO}/issues?state=all"
    )

    response = requests.get(
        url,
        headers=github_headers(token)
    )

    response.raise_for_status()

    return response.json()


def issue_exists(issues, hu_id):

    marker = f"HU-ID: {hu_id}"

    for issue in issues:

        body = issue.get("body", "")

        if marker in body:
            return True

    return False


def extract_hu_id(body):

    if not body:
        return None

    match = re.search(r"<!--\s*HU-ID:\s*(.*?)\s*-->", body)

    if match:
        return match.group(1).strip()

    return None


def build_existing_issue_index(issues):

    index = {}

    for issue in issues:
        hu_id = extract_hu_id(issue.get("body", ""))

        if hu_id:
            index[hu_id] = issue

    return index


def issue_body(issue):

    return f"""
<!-- HU-ID: {issue['id']} -->

{issue['body']}
"""


def normalize_issue_labels(labels):

    normalized = []

    for label in labels:
        if isinstance(label, dict):
            normalized.append(label.get("name", ""))
        else:
            normalized.append(str(label))

    return sorted([label for label in normalized if label])


def create_issue(token, issue):

    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{REPO}/issues"
    )

    payload = {
        "title": issue["title"],
        "body": issue_body(issue),
        "labels": issue.get("labels", [])
    }

    response = requests.post(
        url,
        headers=github_headers(token),
        json=payload
    )

    response.raise_for_status()

    print(
        f"✅ Issue creado: {issue['title']}"
    )


def update_issue(token, existing_issue, issue):

    url = (
        f"https://api.github.com/repos/"
        f"{OWNER}/{REPO}/issues/{existing_issue['number']}"
    )

    payload = {
        "title": issue["title"],
        "body": issue_body(issue),
        "labels": issue.get("labels", [])
    }

    response = requests.patch(
        url,
        headers=github_headers(token),
        json=payload
    )

    response.raise_for_status()

    print(
        f"♻️ Issue actualizada: {issue['title']}"
    )


# ==========================================================
# Backlog & Prompt
# ==========================================================

def load_backlog():

    with open(
            "backlog/backlog.md",
            encoding="utf-8"
    ) as f:
        return f.read()


def load_prompt():

    with open(
            "scripts/prompt.txt",
            encoding="utf-8"
    ) as f:
        return f.read()


def list_available_model_names():

    headers = {
        "Authorization": f"Bearer {MODELS_TOKEN}"
    }

    response = requests.get(
        "https://models.inference.ai.azure.com/models",
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    models = response.json()
    names = []

    for item in models:
        model_id = item.get("id", "")

        # Convierte IDs largos de azureml://.../models/<name>/versions/<n>
        # a nombres cortos útiles para configurar MODELS_MODEL.
        match = re.search(r"/models/([^/]+)/versions/", model_id)

        if match:
            names.append(match.group(1))

    return sorted(set(names))


# ==========================================================
# GitHub Models
# ==========================================================

def generate_issues_from_ai(backlog):

    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=MODELS_TOKEN
    )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": load_prompt()
                },
                {
                    "role": "user",
                    "content": backlog
                }
            ]
        )
    except BadRequestError as exc:
        error_payload = getattr(exc, "body", {}) or {}
        error_details = error_payload.get("error", {})
        code = error_details.get("code")

        if code == "unavailable_model":
            available = []

            try:
                available = list_available_model_names()
            except Exception:
                # Si no se puede consultar catálogo, igualmente devolvemos
                # un mensaje útil con la causa principal.
                available = []

            hint = ""

            if available:
                hint = (
                    " Modelos disponibles para este token: "
                    + ", ".join(available)
                    + "."
                )

            raise RuntimeError(
                f"El modelo '{MODEL_NAME}' no está disponible para este token."
                " Configura MODELS_MODEL en tu .env con un modelo permitido,"
                f" por ejemplo 'gpt-4o-mini'.{hint}"
            ) from exc

        raise

    content = (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

    if content.startswith("```json"):
        content = content.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

    return json.loads(content)


# ==========================================================
# Main
# ==========================================================

def main():

    validate_required_env()

    print("📖 Leyendo backlog...")

    backlog = load_backlog()

    print("🤖 Generando issues...")

    generated_issues = (
        generate_issues_from_ai(backlog)
    )

    print(
        f"✅ La IA ha generado "
        f"{len(generated_issues)} issues"
    )

    token = get_installation_token()

    existing_issues = (
        list_existing_issues(token)
    )

    existing_issue_index = build_existing_issue_index(existing_issues)

    for issue in generated_issues:

        hu_id = issue["id"]

        existing_issue = existing_issue_index.get(hu_id)

        if existing_issue:

            if (
                existing_issue.get("title") == issue["title"]
                and existing_issue.get("body", "").strip() == issue_body(issue).strip()
                and normalize_issue_labels(existing_issue.get("labels", []))
                == normalize_issue_labels(issue.get("labels", []))
            ):
                print(f"⏭️ Ya existe {hu_id} (sin cambios)")
                continue

            update_issue(token, existing_issue, issue)
            continue

        create_issue(
            token,
            issue
        )

    print("✅ Finalizado")

if __name__ == "__main__":
    main()