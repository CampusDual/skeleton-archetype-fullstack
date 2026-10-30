# ${rootArtifactId} (guía rápida)

Este proyecto es una base completa con **backend Java (Spring Boot)**, **frontend Angular** y **base de datos**.  
La idea es que puedas arrancarlo, probarlo y entender la estructura sin necesitar experiencia avanzada.

## Qué puedes hacer con este proyecto

- Iniciar sesión desde frontend.
- Consumir una API REST de usuarios (`/api/users`).
- Probar endpoints desde Swagger.
- Trabajar con 3 modos de ejecución del backend: `v`, `p`, `sp`.
- Usar una base en memoria, una base local persistente o PostgreSQL.

## Estructura del proyecto y para qué sirve cada módulo

| Módulo/carpeta | Qué contiene |
|---|---|
| `${rootArtifactId}-api` | Contratos: DTOs e interfaces de servicio (qué se expone). |
| `${rootArtifactId}-model` | Lógica de negocio, entidades JPA y repositorios (cómo se guarda y valida). |
| `${rootArtifactId}-ws` | Controladores REST y seguridad (endpoints HTTP y control de acceso). |
| `${rootArtifactId}-openapi` | Especificación OpenAPI (`openapi.yaml` y `openapi-copilot.yaml`). |
| `${rootArtifactId}-boot` | Arranque Spring Boot, configuración por perfiles y migraciones de base de datos. |
| `${rootArtifactId}-frontend` | Aplicación Angular (login + pantalla privada + llamadas al backend). |
| `.run` | Lanzadores preparados para IntelliJ (`V`, `P`, `SP` y `DB`). |
| `.github/copilot-instructions.md` | Reglas del proyecto para asistente/copilot (fuente de verdad). |

## Versiones

Estas son las versiones que se utilizaron en este proyecto:

| Herramienta | Versión |
|---|---|
| Node.js | `23.6.0` |
| npm | `10.9.2` |
| Maven | `3.9.10` |
| Java | `25.0.4.1` (Eclipse Adoptium) |
| Angular CLI | `19.2.27` |

> Importante sobre Node.js: Angular CLI marca `23.6.0` como **Unsupported**, por no ser una versión LTS.

## Modos de lanzamiento del backend (`v`, `p`, `sp`)

### 1) Modo `v` (rápido para empezar)
- Usa base **en memoria** (no guarda datos al cerrar).
- Es el más simple para practicar.

**En IntelliJ**
1. Ejecuta `V - ${rootArtifactId}Application`.

**Alternativa Maven**
```bash
mvn -pl ${rootArtifactId}-boot spring-boot:run -Dspring-boot.run.profiles=v
```

---

### 2) Modo `p` (persistente en local)
- Usa HSQLDB en archivo local (`.local/hsqldb/appdb`), así los datos **se conservan**.
- Necesita **arrancar la base de datos antes** que el backend.
- Puedes consultar la BD desde la consola H2 del navegador, pero para trabajo más cómodo normalmente también se usan clientes externos como **DBeaver**.

**En IntelliJ (orden obligatorio)**
1. Ejecuta `DB - HSQLDB Server`.
2. Ejecuta `P - ${rootArtifactId}Application`.

**Alternativa Maven (dos terminales)**
Terminal 1 (BD):
```bash
mvn -pl ${rootArtifactId}-boot -Prun_database validate exec:java
```
Terminal 2 (backend):
```bash
mvn -pl ${rootArtifactId}-boot -Prun_app_p spring-boot:run
```

---

### 3) Modo `sp` (PostgreSQL)
- Usa PostgreSQL en `localhost:5432`, base `appdb`.
**En IntelliJ**
1. Asegúrate de tener PostgreSQL levantado con esa base.
2. Ejecuta `SP - ${rootArtifactId}Application`.

**Alternativa Maven**
```bash
mvn -pl ${rootArtifactId}-boot spring-boot:run -Dspring-boot.run.profiles=sp
```

## URLs importantes (cuando backend está arrancado)

| Uso | URL |
|---|---|
| Backend (base) | `http://localhost:8080` |
| Swagger UI | `http://localhost:8080/swagger-ui/index.html` |
| OpenAPI automática | `http://localhost:8080/v3/api-docs` |
| OpenAPI Copilot (manual) | `http://localhost:8080/openapi-copilot.yaml` |
| Consola H2 (navegador) | `http://localhost:8080/h2-console` |

> La consola web de BD incluida en el proyecto es la de H2 (`/h2-console`) y funciona bien para pruebas rápidas.  
> Aun así, para consultas más largas, filtros, exportaciones y manejo avanzado, lo habitual es usar un cliente externo.
> - En modo `p` (HSQLDB persistente): Suele resultar más práctico usar herramientas externas como **DBeaver**.
> - En modo `sp` (PostgreSQL): Normalmente se utiliza **pgAdmin** o **DBeaver**.

## Frontend: cómo lanzarlo desde Visual Studio Code (cuando backend está arrancado)

Abre una terminal en `${rootArtifactId}-frontend` y ejecuta:

```bash
npm install
npm start
```

Luego abre:

```text
http://localhost:4200
```

Notas útiles:
- El frontend tiene proxy configurado: las llamadas a `/api` se redirigen a `http://localhost:8080`.
- Si backend no está levantado, el login mostrará error de conexión.

## Usuario inicial

En el arranque se crea un usuario admin:
- usuario: `admin`
- contraseña: `admin1234`

## Flujo recomendado para empezar

1. Arranca backend en modo `v`.
2. Arranca frontend (`npm start`).
3. Entra en `http://localhost:4200` con `admin / admin1234`.
4. Revisa Swagger en `http://localhost:8080/swagger-ui/index.html`.

## Comandos de comprobación de compilación

En la raíz del proyecto:

```bash
mvn compile
mvn test-compile
```

## Archivo de instrucciones de Copilot

El proyecto incluye reglas específicas en:

```text
.github/copilot-instructions.md
```

Ahí se define, entre otras cosas:
- estructura esperada de módulos
- convenciones de código/documentación
- cómo mantener los ficheros de openapi
- reglas de ejecución en terminal para el equipo
