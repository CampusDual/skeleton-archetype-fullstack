[![Fullstack Archetype](https://img.shields.io/maven-central/v/com.campusdual/skeleton-fullstack-archetype?label=Latest%20fullstack%20archetype&style=flat-square)](https://central.sonatype.com/artifact/com.campusdual/skeleton-fullstack-archetype)

# Campus Dual Fullstack Archetype - base project

This repository is the **base application** used to generate Campus Dual fullstack Maven archetype.  
Any change that should appear in newly generated projects must be implemented here and published through the archetype GitHub Action.

## What does this archetype include?

- Spring Boot multi-module backend:
  - `<artifactId>-api`
  - `<artifactId>-model`
  - `<artifactId>-ws`
  - `<artifactId>-openapi`
  - `<artifactId>-boot`
- Angular frontend:
  - `<artifactId>-frontend`
- `.run` configurations adapted to the generated `artifactId`.

## Generation and deployment flow

Archetype publishing is handled by:

- `.github/workflows/deploy-archetype.yml`

This workflow:

1. Removes elements that should not be part of the final template.
2. Runs `mvn archetype:create-from-project`.
3. Normalizes placeholders and paths (modules, frontend, Java packages, `.run`, OpenAPI, etc.).
4. Deploys `99.9.9-SNAPSHOT` by default.
5. Optionally deploys a RELEASE version when `custom-version` is provided.
6. Uploads a generated test project (`fullstack-zip`) as a workflow artifact.

## Using the archetype

> [!WARNING]
> Replace these sample values with your own: `YOUR_PROJECT_GROUP_ID`, `YOUR_PROJECT_ARTIFACT_ID`, `YOUR_PROJECT_VERSION`, `YOUR_PROJECT_PACKAGE`, and `LAST_VERSION`.

> [!TIP]
> In PowerShell, wrap each `-D...` parameter in double quotes.

### Latest RELEASE version

[![Fullstack Archetype Release](https://img.shields.io/maven-central/v/com.campusdual/skeleton-fullstack-archetype?label=&style=flat-square)](https://central.sonatype.com/artifact/com.campusdual/skeleton-fullstack-archetype)

```bash
mvn -B archetype:generate -DgroupId=YOUR_PROJECT_GROUP_ID -DartifactId=YOUR_PROJECT_ARTIFACT_ID -Dversion=YOUR_PROJECT_VERSION -Dpackage=YOUR_PROJECT_PACKAGE -DarchetypeGroupId=com.campusdual -DarchetypeArtifactId=skeleton-fullstack-archetype -DarchetypeVersion=LAST_VERSION -DinteractiveMode=false
```

### Latest SNAPSHOT version

```bash
mvn -B archetype:generate -DgroupId=YOUR_PROJECT_GROUP_ID -DartifactId=YOUR_PROJECT_ARTIFACT_ID -Dversion=YOUR_PROJECT_VERSION -Dpackage=YOUR_PROJECT_PACKAGE -DarchetypeGroupId=com.campusdual -DarchetypeArtifactId=skeleton-fullstack-archetype -DarchetypeVersion=99.9.9-SNAPSHOT -DinteractiveMode=false
```

## Why use `99.9.9-SNAPSHOT`?

It is used as the **latest** version so the archetype can be continuously updated without changing the base project version on every internal iteration.  
When a stable release is needed, the same workflow can publish a specific RELEASE via `custom-version`.

## How to test the archetype

### Option 1: from GitHub Actions artifact

In a `deploy-archetype.yml` run, download `fullstack-zip` and extract the `.tar.gz` to inspect the generated project.

### Option 2: with a local Maven command

```bash
mvn -B archetype:generate -DgroupId=com.campusdual -DartifactId=fullstacktest -Dversion=1.0.0-SNAPSHOT -Dpackage=com.campusdual.fullstacktest -DarchetypeGroupId=com.campusdual -DarchetypeArtifactId=skeleton-fullstack-archetype -DarchetypeVersion=99.9.9-SNAPSHOT -DinteractiveMode=false
```

## FAQ

### Error: `99.9.9-SNAPSHOT` version not found

By default, Maven may not resolve SNAPSHOT versions from Central.  
You need to enable snapshots in `~/.m2/settings.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
  <profiles>
    <profile>
      <id>central</id>
      <repositories>
        <repository>
          <id>central-snapshots</id>
          <url>https://central.sonatype.com/repository/maven-snapshots/</url>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
          <releases>
            <enabled>false</enabled>
          </releases>
        </repository>
      </repositories>
    </profile>
  </profiles>
  <activeProfiles>
    <activeProfile>central</activeProfile>
  </activeProfiles>
</settings>
```

If you do not want to use SNAPSHOT versions, use the latest RELEASE available in Maven Central.

## Maintenance notes

- The README that generated projects will receive is `HELP.md` (the workflow renames it to `README.md` in the final template).
- If you change modules, structure, or placeholders, also review the **Normalize archetype resources** phase in `deploy-archetype.yml`.
