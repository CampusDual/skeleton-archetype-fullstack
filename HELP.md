# Campus Dual Fullstack Archetype

Este README se inyecta automáticamente en los proyectos generados desde el arquetipo.

## ¿Qué incluye el arquetipo?

- Estructura backend multi-módulo Spring Boot:
  - `stockrestaurante-api`
  - `stockrestaurante-model`
  - `stockrestaurante-ws`
  - `stockrestaurante-openapi`
  - `stockrestaurante-boot`
- Carpeta frontend Angular nombrada con el `artifactId` del proyecto:
  - `<artifactId>-frontend`

## Generar un proyecto desde Maven

Sustituye los valores de ejemplo por los de tu proyecto:

```bash
mvn -B archetype:generate \
  -DgroupId=YOUR_PROJECT_GROUP_ID \
  -DartifactId=YOUR_PROJECT_ARTIFACT_ID \
  -Dversion=YOUR_PROJECT_VERSION \
  -Dpackage=YOUR_PROJECT_PACKAGE \
  -DarchetypeGroupId=com.campusdual \
  -DarchetypeArtifactId=skeleton-fullstack-archetype \
  -DarchetypeVersion=99.9.9-SNAPSHOT \
  -DinteractiveMode=false
```

> En PowerShell de Windows, recuerda envolver cada `-D...` entre comillas dobles.

## Sobre la versión `99.9.9-SNAPSHOT`

Se usa como versión "latest" del arquetipo para poder publicar iteraciones sin tener que cambiar la coordenada del proyecto base.
