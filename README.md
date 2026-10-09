# stock Restaurante

<details>
<summary><strong>💡 Stock Restaurante - Funcional</strong></summary>

Ejemplo práctico para que un Product Owner (PO) pase de un problema de negocio a una lista de issues implementables con apoyo de IA.

## Objetivo del flujo

Este repositorio ilustra este recorrido completo:

```text
Problema de negocio
    -> Discovery
    -> Especificacion funcional
    -> Requisitos y diseno
    -> Backlog de historias
    -> Issues en GitHub
```

El foco es separar claramente:
- lo que valida y decide el PO (manual),
- y lo que la IA acelera o automatiza.

## Mapa rapido del repositorio

- `01-discovery/01-first-analisys-prompts/01-first-analisys-prompt.md`: prompt para que la IA estructure el analisis del problema.
- `01-discovery/01-first-analisys-prompts/01r-result-example.md`: discovery resultante (problema, impacto, riesgos, metricas).
- `01-discovery/02-miro-prompts/01-value-proposition-canvas.md`: prompt para generar Value Proposition Canvas.
- `01-discovery/02-miro-prompts/02-business-model-canvas.md`: prompt para generar Business Model Canvas.
- `01-discovery/02-miro-prompts/04-customer-journey.md`: prompt para generar Customer Journey Map.
- `01-discovery/02-miro-prompts/05-user-story-mapping.md`: prompt para User Story Mapping (requiere salidas de los 3 prompts anteriores).
- `01-discovery/02-miro-prompts/06-MVP.md`: espacio para consolidar el MVP priorizado tras el user story mapping.
- `02-specs/prompt.txt`: prompt para convertir discovery en especificacion funcional.
- `02-specs/inventory-management-spec.md`: especificacion funcional de referencia.
- `02-specs/inventory-management/requirements.md`: requisitos funcionales resumidos.
- `02-specs/inventory-management/design.md`: diseno funcional/tactico.
- `02-specs/inventory-management/tasks.md`: tareas por epica (base para implementacion).
- `03-backlog/prompt.xt`: prompt para convertir especificacion en historias de usuario.
- `03-backlog/backlog.md`: backlog en formato HU con criterios de aceptacion.
- `04-github-issues-gen/prompt.txt`: prompt que obliga a devolver JSON de issues.
- `04-github-issues-gen/generate_issues.py`: crea o actualiza issues reales en GitHub.

## Walkthrough PO paso a paso

### Paso 0 - Preparar entorno (una vez)

**PO hace manualmente**
- Configurar Python y dependencias.
- Crear archivo `.env` con credenciales.

**IA automatiza**
- Nada en este paso (es setup operativo).

Comandos:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Variables requeridas en `.env`:
- `MODELS_TOKEN`
- `MODELS_MODEL` (opcional, por defecto `gpt-4o-mini`)
- `APP_ID`
- `INSTALLATION_ID`
- `OWNER`
- `REPO`
- `PRIVATE_KEY_PATH` (opcional, por defecto `github-app.pem`)

---

### Paso 1 - Definir el problema de negocio

**PO hace manualmente**
- Redactar el problema inicial en lenguaje de negocio.
- Aportar contexto: impacto, clientes afectados, coste de no resolverlo.

**IA automatiza**
- Aun no genera entregables finales; aqui recibe contexto.

Ejemplo de input del PO:

```text
"En mi restaurante tengo problemas para controlar el stock..."
```

---

### Paso 2 - Generar Discovery

**PO hace manualmente**
- Revisar `01-discovery/01-first-analisys-prompts/01r-result-example.md` y corregir supuestos.
- Validar que existan objetivos medibles y riesgos.

**IA automatiza**
- Estructura el discovery usando `01-discovery/01-first-analisys-prompts/01-first-analisys-prompt.md`.

**Como lanza la accion automatica el PO**
- En el chat de IA del IDE: pedir que use `01-discovery/01-first-analisys-prompts/01-first-analisys-prompt.md` con el problema de negocio y que escriba/actualice `01-discovery/01-first-analisys-prompts/01r-result-example.md`.

Prompt sugerido para el PO:

```text
Usa la plantilla de 01-discovery/prompt.md con este problema de negocio y genera/actualiza 01-discovery/description.md.
```

---

### Paso 2.5 - Validar estrategia con prompts de Miro

**PO hace manualmente**
- Ejecutar los prompts en este orden: Value Proposition Canvas -> Business Model Canvas -> Customer Journey -> User Story Mapping.
- Adjuntar al prompt de User Story Mapping las salidas de los 3 pasos anteriores.
- Si no se comparten los tableros Miro, adjuntar su contenido exportado (CSV, texto, markdown, JSON o capturas) para que la IA tenga el contexto completo.

**IA automatiza**
- Genera cada diagrama a partir del artefacto anterior.
- En `05-user-story-mapping.md`, combina Discovery + VPC + BMC + Customer Journey para construir actividades, historias y releases.

**Como lanza la accion automatica el PO**
- En el chat de IA: ejecutar cada prompt en secuencia y guardar/adjuntar salidas antes del siguiente.

Prompt sugerido:

```text
Usa 01-discovery/02-miro-prompts/04-user-story-mapping.md y toma como entrada discovery + resultados de VPC, BMC y Customer Journey. Si los diagramas no estan en Miro, usa sus exportaciones adjuntas (CSV/texto/markdown/JSON/capturas).
```

---

### Paso 3 - Generar Especificacion funcional

**PO hace manualmente**
- Verificar alcance MVP, exclusiones, no funcionales y criterios de exito.
- Aprobar version de trabajo de especificacion.

**IA automatiza**
- Toma discovery + `02-specs/prompt.txt` y genera la especificacion.

**Como lanza la accion automatica el PO**
- En el chat de IA: solicitar la generacion de `02-specs/inventory-management-spec.md` desde `01-discovery/01-first-analisys-prompts/01r-result-example.md` usando `02-specs/prompt.txt`.

Prompt sugerido:

```text
Usa specs/prompt.txt y 01-discovery/description.md para generar/actualizar specs/inventory-management-spec.md.
```

---

### Paso 4 - Refinar a requisitos, diseno y tareas

**PO hace manualmente**
- Validar trazabilidad (cada objetivo del negocio debe tener requisitos y tareas).
- Priorizar que entra en MVP y que queda fuera.

**IA automatiza**
- Propone o actualiza:
  - `02-specs/inventory-management/requirements.md`
  - `02-specs/inventory-management/design.md`
  - `02-specs/inventory-management/tasks.md`

**Como lanza la accion automatica el PO**
- En el chat de IA: pedir actualizacion de los 3 artefactos a partir de la especificacion funcional.

Prompt sugerido:

```text
A partir de specs/inventory-management-spec.md, actualiza requirements.md, design.md y tasks.md en specs/inventory-management/.
```

---

### Paso 5 - Generar backlog de historias de usuario

**PO hace manualmente**
- Revisar historias, criterios Gherkin y prioridades.
- Confirmar orden de ejecucion y dependencias.

**IA automatiza**
- Convierte especificacion en backlog (`03-backlog/backlog.md`) usando `03-backlog/prompt.xt`.

**Como lanza la accion automatica el PO**
- En el chat de IA: pedir la generacion de backlog desde especificacion.

Prompt sugerido:

```text
Usa 02-backlog/prompt.xt y specs/inventory-management-spec.md para generar/actualizar 02-backlog/backlog.md.
```

---

### Paso 6 - Publicar issues implementables en GitHub

**PO hace manualmente**
- Comprobar `.env` y permisos de GitHub App.
- Ejecutar el script y revisar los issues creados/actualizados.

**IA automatiza**
- `04-github-issues-gen/generate_issues.py`:
  - lee backlog y prompt,
  - pide a GitHub Models una lista JSON de issues,
  - crea o actualiza issues por HU-ID (idempotente).

**Como lanza la accion automatica el PO**

```powershell
python scripts/generate_issues.py
```

---

## Quien hace que (resumen ejecutivo)

- **PO manual**: define problema, valida supuestos, prioriza MVP, aprueba backlog.
- **IA asistida (chat)**: redacta discovery, especificacion, requisitos/diseno/tareas y backlog.
- **IA automatizada (script)**: transforma backlog a issues y los publica en GitHub.

## Notas practicas

- Actualmente `04-github-issues-gen/generate_issues.py` lee `03-backlog/backlog.md`.
- En este repo el backlog esta en `03-backlog/backlog.md`.
- Si no se ajusta la ruta, la ejecucion puede fallar por archivo no encontrado.

## Instalacion de Spec Kit (opcional)

Si quieres trabajar con comandos de Spec Kit:

```powershell
pip install uv
uv tool install specify-cli
specify --version
specify init .
```

Si IntelliJ no encuentra `specify`, verifica la ruta:

```powershell
where.exe specify
```

</details>

<details>
<summary><strong>­ƒøá´©Å Stock Restaurante - T├®cnico</strong></summary>

Proyecto base Spring Boot multi-modulo para arrancar desde cero con seguridad y gestion de usuarios.

## Modulos

- `stockrestaurante-api`: contratos de servicio y DTOs de usuarios.
- `stockrestaurante-model`: entidades de usuario/rol, repositorios y logica de negocio.
- `stockrestaurante-ws`: controladores REST de usuarios, seguridad y manejo de errores HTTP.
- `stockrestaurante-openapi`: contrato OpenAPI (`openapi.yaml`).
- `stockrestaurante-boot`: arranque de Spring Boot y configuracion.

## Requisitos

- JDK 25
- Maven 3.9+

## Arranque rapido

```powershell
mvn clean test
mvn -pl stockrestaurante-boot spring-boot:run
```

## Base de datos y perfiles

- `v` (por defecto implicito): HSQLDB en memoria, base nueva en cada arranque.
- `p`: HSQLDB por TCP para acceso externo (DBeaver) y persistencia en fichero local.
- `sp`: PostgreSQL compartido/remoto.

Arranques recomendados:

```powershell
# v implicito (HSQLDB en memoria)
mvn -pl stockrestaurante-boot spring-boot:run

# p (arranca primero HSQLDB TCP y luego la app)
# terminal 1
mvn -pl stockrestaurante-boot -Prun_database exec:java

# terminal 2
mvn -pl stockrestaurante-boot -Prun_app_p spring-boot:run

# sp (PostgreSQL)
mvn -pl stockrestaurante-boot spring-boot:run -Dspring-boot.run.profiles=sp
```

Conexion DBeaver para perfil `p`:

- Host: `localhost`
- Puerto: `9001`
- Database: `stockdb`
- Usuario: `sa`
- Password: vacia

## Seguridad por defecto

- La API requiere autenticacion para todos los endpoints.
- Las operaciones de escritura de usuarios (`POST`, `PUT`, `DELETE`) requieren rol `ADMIN`.
- Usuario semilla al arrancar por primera vez:
  - username: `admin`
  - password: `admin1234`

## Cambiar a PostgreSQL

1. Crea la base de datos en PostgreSQL, por ejemplo `stockrestaurante`.
2. Ajusta credenciales en `stockrestaurante-boot/src/main/resources/application-sp.yml`.
3. Arranca con el perfil:

```powershell
mvn -pl stockrestaurante-boot spring-boot:run -Dspring-boot.run.profiles=sp
```

## Endpoints de ejemplo

- `GET /api/users`
- `POST /api/users`
- `GET /api/users/{id}`
- `PUT /api/users/{id}`
- `DELETE /api/users/{id}`

</details>
