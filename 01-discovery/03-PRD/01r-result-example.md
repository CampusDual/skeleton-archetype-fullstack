# Hallazgos del análisis

## Inconsistencias detectadas

No se identifican contradicciones explícitas en la información suministrada. El problema, oportunidad, usuarios, hipótesis, métricas y riesgos mantienen coherencia entre sí.

## Lagunas de información

### Negocio
- No se especifica si la solución será SaaS multiempresa o una instalación por restaurante.
- No se define el modelo de monetización.
- No se indica el tamaño objetivo de los restaurantes (individuales, cadenas, franquicias).
- No se especifica el ámbito geográfico.

### Operación
- No se indica cómo se realiza actualmente el inventario inicial.
- No se especifica la frecuencia de reposición ni los procesos de compra existentes.
- No se describe el flujo de recepción de mercancía.

### Tecnología
- No se identifica el TPV concreto con el que se integrará la solución.
- No se define la arquitectura deseada.
- No se detallan requisitos regulatorios o de protección de datos específicos.

### Producto
- No se detalla el nivel de automatización esperado para los pedidos.
- No se especifica si la disponibilidad de platos afecta solamente al personal interno o también a cartas digitales y canales online.
- No se indica si se gestionarán múltiples almacenes.

## Hipótesis necesarias para elaborar el PRD

1. La solución será un producto SaaS.
2. La plataforma se orientará inicialmente a restaurantes individuales y pequeñas cadenas.
3. Existirá integración con al menos un TPV externo.
4. Cada plato consumirá ingredientes mediante una receta configurable.
5. Los usuarios accederán mediante aplicación web responsive.
6. El sistema gestionará al menos un almacén por restaurante.
7. El inventario se actualizará en tiempo real tras la recepción de ventas desde el TPV.

---

# PRODUCT REQUIREMENTS DOCUMENT

# 1. Información General

## 1.1 Nombre del Producto

Gestión Inteligente de Inventario para Restauración

## 1.2 Versión del Documento

v1.0

## 1.3 Fecha

11/09/2026

## 1.4 Estado del Documento

**Draft**

## 1.5 Autores y Stakeholders

### Autores
- Product Manager
- Product Owner
- Equipo de Discovery

### Stakeholders
- Responsable del restaurante
- Responsable de compras
- Gerente
- Camareros
- Clientes finales
- Proveedores
- Equipo de operaciones
- Equipo de desarrollo
- Equipo QA

---

# 2. Resumen Ejecutivo

## 2.1 Descripción del Producto

Plataforma digital que integra inventario, recetas, ventas, compras y analítica para mantener la visibilidad del stock en tiempo real y optimizar la gestión operativa de restaurantes.

## 2.2 Problema de Negocio

Los restaurantes suelen operar con herramientas fragmentadas y procesos manuales que generan errores de inventario, falta de visibilidad, compras ineficientes y experiencia inconsistente para empleados y clientes.

## 2.3 Oportunidad Detectada

Unificar datos de ventas, recetas e inventario para automatizar la gestión del stock y convertir la información operativa en decisiones accionables.

## 2.4 Solución Propuesta

Una plataforma capaz de:

- Gestionar inventario.
- Gestionar recetas.
- Integrarse con TPV.
- Actualizar stock automáticamente.
- Detectar necesidades de reposición.
- Automatizar pedidos.
- Gestionar disponibilidad de platos.
- Generar cuadros analíticos.

## 2.5 Beneficios Esperados

### Para el negocio
- Menos desperdicio.
- Menores roturas de stock.
- Optimización de compras.
- Reducción de costes operativos.

### Para el usuario
- Información fiable.
- Menos tareas manuales.
- Mayor rapidez de gestión.

## 2.6 Resumen del Valor Aportado

La solución transforma la gestión reactiva de inventario en una gestión predictiva y automatizada basada en datos operativos en tiempo real.

---

# 3. Contexto

## 3.1 Situación Actual

- Inventarios manuales.
- Registros dispersos.
- Escasa trazabilidad.
- Dependencia de la experiencia del personal.

## 3.2 Problemas Existentes

- Falta de visibilidad.
- Roturas de stock.
- Compras urgentes.
- Disponibilidad incorrecta de productos.
- Análisis limitado.

## 3.3 Necesidades Detectadas

- Inventario centralizado.
- Actualización automática.
- Gestión de recetas.
- Automatización de compras.
- Analítica avanzada.

## 3.4 Motivadores de Negocio

- Mejorar rentabilidad.
- Reducir errores.
- Optimizar operaciones.
- Aumentar satisfacción del cliente.

## 3.5 Restricciones Conocidas

- Dependencia de integraciones TPV.
- Calidad de datos iniciales.
- Correcta configuración de recetas.

## 3.6 Dependencias

- Sistemas TPV.
- Catálogo de proveedores.
- Configuración de recetas.
- Datos de inventario inicial.

---

# 4. Objetivos del Producto

## 4.1 Objetivos Estratégicos

- Digitalizar la gestión de inventario.
- Crear una operación basada en datos.
- Mejorar rentabilidad del restaurante.

## 4.2 Objetivos Operativos

- Automatizar descuentos de stock.
- Automatizar reposiciones.
- Reducir trabajos manuales.

## 4.3 Objetivos para Usuarios

- Conocer stock real.
- Tomar decisiones rápidamente.
- Evitar errores de disponibilidad.

## 4.4 Objetivos para la Organización

- Disminuir costes.
- Mejorar eficiencia.
- Incrementar control operativo.

---

# 5. Métricas de Éxito

## Métricas de negocio

### KPI-01 Reducción de roturas de stock

- Descripción: Frecuencia de faltantes.
- Fórmula:
    - (Roturas actuales - Roturas posteriores) / Roturas actuales × 100
- Objetivo: ≥ 40%
- Frecuencia: Mensual

### KPI-02 Reducción de compras urgentes

- Fórmula:
    - Compras urgentes / Compras totales
- Objetivo: <10%
- Frecuencia: Mensual

## Métricas de producto

### KPI-03 Precisión del stock

- Fórmula:
    - Unidades correctas / Unidades auditadas
- Objetivo: >95%
- Frecuencia: Semanal

### KPI-04 Disponibilidad correcta de platos

- Fórmula:
    - Platos correctamente informados / Total platos
- Objetivo: >98%
- Frecuencia: Diaria

## Métricas de adopción

### KPI-05 Usuarios activos

- Fórmula:
    - Usuarios activos mensuales
- Objetivo: >85% usuarios registrados
- Frecuencia: Mensual

### KPI-06 Uso de pedidos automatizados

- Fórmula:
    - Pedidos automatizados / Total pedidos
- Objetivo: >60%
- Frecuencia: Mensual

## Métricas operativas

### KPI-07 Tiempo medio de reposición

- Objetivo: Reducir 30%
- Frecuencia: Mensual

### KPI-08 Tiempo dedicado al inventario

- Objetivo: Reducir 50%
- Frecuencia: Mensual

## Métricas de satisfacción

### KPI-09 NPS

- Objetivo: >40
- Frecuencia: Trimestral

### KPI-10 CSAT

- Objetivo: >4/5
- Frecuencia: Mensual

---

# 6. Segmentos de Usuarios

## 6.1 Tipología de usuarios

### Operativos
- Responsable restaurante
- Responsable compras

### Supervisión
- Gerente

### Ejecución
- Camarero

### Consumo
- Cliente

## 6.2 Personas identificadas

### Persona 1: Responsable del Restaurante

**Perfil**
Encargado de operaciones diarias.

**Objetivos**
- Controlar existencias.
- Evitar roturas.

**Motivaciones**
- Eficiencia operativa.

**Frustraciones**
- Inventarios incorrectos.

**Necesidades**
- Visibilidad en tiempo real.

### Persona 2: Responsable de Compras

**Perfil**
Gestiona proveedores y pedidos.

**Objetivos**
- Comprar en el momento adecuado.

**Motivaciones**
- Optimización de costes.

**Frustraciones**
- Pedidos urgentes.

**Necesidades**
- Alertas y recomendaciones.

### Persona 3: Gerente

**Perfil**
Responsable del rendimiento del negocio.

**Objetivos**
- Mejorar rentabilidad.

**Motivaciones**
- Toma de decisiones basada en datos.

**Frustraciones**
- Falta de indicadores.

**Necesidades**
- Dashboards.

### Persona 4: Camarero

**Perfil**
Empleado de atención al cliente.

**Objetivos**
- Conocer disponibilidad real.

**Motivaciones**
- Buen servicio.

**Frustraciones**
- Ofrecer platos agotados.

**Necesidades**
- Información actualizada.

### Persona 5: Cliente

**Perfil**
Consumidor final.

**Objetivos**
- Pedir productos disponibles.

**Motivaciones**
- Buena experiencia.

**Frustraciones**
- Indisponibilidad inesperada.

**Necesidades**
- Información veraz.

---

# 7. Actor Mapping

## Actores Primarios

### Responsable del Restaurante

- Descripción: Gestor operativo principal.
- Interacciones: Inventario, recetas, alertas.
- Influencia: Alta.
- Interés: Muy alto.
- Relación: Gerente, compras y camareros.

### Responsable de Compras

- Descripción: Gestiona aprovisionamiento.
- Interacciones: Pedidos y proveedores.
- Influencia: Alta.
- Interés: Muy alto.

### Camarero

- Descripción: Consulta disponibilidad.
- Influencia: Media.
- Interés: Alto.

## Actores Secundarios

### Gerente

- Supervisión de KPIs.
- Influencia alta.
- Interés alto.

## Actores Externos

### Cliente

- Consume información de disponibilidad.
- Influencia indirecta.
- Interés alto.

### Proveedor

- Recibe pedidos.
- Actualiza suministro.
- Influencia media.

### Sistema TPV

- Fuente de ventas.
- Influencia crítica.

---

# 8. Customer Journey

## Descubrimiento

- Objetivo: Resolver problemas de inventario.
- Acciones: Evaluar solución.
- Touchpoints: Web comercial, demos.
- Emociones: Curiosidad.
- Pain points: Falta de confianza.
- Oportunidades: Casos de éxito.

## Configuración

- Objetivo: Poner en marcha sistema.
- Acciones: Cargar stock y recetas.
- Touchpoints: Plataforma.
- Emociones: Expectativa.
- Pain points: Complejidad inicial.
- Oportunidades: Asistentes guiados.

## Operación Diaria

- Objetivo: Gestionar inventario.
- Acciones: Ventas, reposición, consultas.
- Touchpoints: Dashboard y TPV.
- Emociones: Confianza.
- Pain points: Integraciones.
- Oportunidades: Automatización.

## Optimización

- Objetivo: Mejorar resultados.
- Acciones: Analizar indicadores.
- Touchpoints: Cuadros analíticos.
- Emociones: Satisfacción.
- Pain points: Calidad de datos.
- Oportunidades: IA predictiva.

---

# 9. Alcance del Producto

## 9.1 Alcance Incluido

- Gestión de inventario.
- Gestión de recetas.
- Sincronización TPV.
- Disponibilidad de platos.
- Compras y reposición.
- Analítica.

## 9.2 Alcance Excluido

- Gestión financiera completa.
- RRHH.
- Nómina.
- CRM.
- Gestión logística avanzada.

## 9.3 Supuestos

- TPV integrable.
- Recetas correctamente configuradas.
- Inventario inicial fiable.

## 9.4 Limitaciones

- Dependencia de integraciones.
- Calidad de datos de origen.

---

# 10. Propuesta de Valor

## 10.1 Value Proposition

Control inteligente del inventario basado en ventas reales y recetas configuradas.

## 10.2 Beneficios Funcionales

- Stock en tiempo real.
- Automatización.
- Analítica.

## 10.3 Beneficios Emocionales

- Tranquilidad.
- Confianza.
- Control.

## 10.4 Diferenciadores Competitivos

- Integración inventario-receta-venta.
- Automatización de pedidos.
- Disponibilidad dinámica.

## 10.5 Ventajas frente a alternativas

- Menor trabajo manual.
- Mayor precisión.
- Mayor visibilidad.

---

# 11. Requisitos Funcionales

## RF-001 - Gestión de Inventario

- Descripción: Crear, actualizar y consultar inventario.
- Justificación: Disponer de visibilidad continua de existencias.
- Actor implicado: Responsable del restaurante.
- Prioridad: Must Have.
- Dependencias: Ninguna.

## RF-002 - Gestión de Recetas

- Descripción: Configurar platos e ingredientes asociados.
- Justificación: Calcular consumos automáticamente.
- Actor implicado: Responsable del restaurante.
- Prioridad: Must Have.
- Dependencias: RF-001.

## RF-003 - Integración TPV

- Descripción: Sincronización de ventas desde TPV.
- Justificación: Actualización automática del stock.
- Actor implicado: Sistema TPV.
- Prioridad: Must Have.
- Dependencias: Integración externa.

## RF-004 - Descuento Automático de Stock

- Descripción: Descontar ingredientes consumidos tras cada venta.
- Justificación: Mantener precisión del inventario.
- Actor implicado: Sistema.
- Prioridad: Must Have.
- Dependencias: RF-002, RF-003.

## RF-005 - Disponibilidad de Platos

- Descripción: Calcular disponibilidad de platos en tiempo real.
- Justificación: Evitar ofrecer productos agotados.
- Actor implicado: Camarero.
- Prioridad: Must Have.
- Dependencias: RF-004.

## RF-006 - Alertas de Reposición

- Descripción: Generar alertas cuando se alcancen umbrales mínimos.
- Justificación: Reducir roturas de stock.
- Actor implicado: Responsable de compras.
- Prioridad: Must Have.
- Dependencias: RF-001.

## RF-007 - Pedidos Automatizados

- Descripción: Generar pedidos sugeridos automáticamente.
- Justificación: Reducir trabajo manual.
- Actor implicado: Responsable de compras.
- Prioridad: Should Have.
- Dependencias: RF-006.

## RF-008 - Gestión de Proveedores

- Descripción: Mantener catálogo de proveedores.
- Justificación: Facilitar reposiciones.
- Actor implicado: Responsable de compras.
- Prioridad: Should Have.
- Dependencias: RF-007.

## RF-009 - Dashboard Analítico

- Descripción: Visualizar KPIs e indicadores.
- Justificación: Favorecer decisiones basadas en datos.
- Actor implicado: Gerente.
- Prioridad: Should Have.
- Dependencias: RF-001, RF-003.

## RF-010 - Auditoría

- Descripción: Registrar movimientos e histórico.
- Justificación: Garantizar trazabilidad.
- Actor implicado: Gerente.
- Prioridad: Should Have.
- Dependencias: Todos los módulos.

---

# 12. Funcionalidades del Producto

## Gestión de Inventario

### Objetivo
Controlar existencias.

### Descripción
Permite registrar, consultar, ajustar y auditar inventarios.

### Flujo principal
Entrada → Consulta → Ajuste → Auditoría

### Variantes
- Carga manual.
- Importación masiva.

### Beneficio aportado
Visibilidad completa del stock.

### Prioridad
Must Have

## Gestión de Recetas

### Objetivo
Relacionar platos con ingredientes.

### Descripción
Configuración del consumo teórico de ingredientes.

### Flujo principal
Crear receta → Asociar ingredientes → Definir cantidades → Publicar

### Variantes
- Edición de receta.
- Versionado.

### Beneficio aportado
Automatización del control de consumo.

### Prioridad
Must Have

## Sincronización TPV

### Objetivo
Actualizar stock automáticamente.

### Descripción
Recepción de ventas y actualización inmediata.

### Flujo principal
Venta → Sincronización → Cálculo → Actualización

### Variantes
- Sincronización batch.
- Reprocesamiento.

### Beneficio aportado
Eliminación de tareas manuales.

### Prioridad
Must Have

## Alertas de Reposición

### Objetivo
Evitar roturas de stock.

### Descripción
Notificaciones cuando se alcanzan mínimos.

### Flujo principal
Monitorización → Detección → Notificación

### Variantes
- Correo.
- Notificación interna.

### Beneficio aportado
Reposición preventiva.

### Prioridad
Must Have

## Automatización de Pedidos

### Objetivo
Reducir trabajo manual.

### Descripción
Generación automática o sugerida de pedidos.

### Flujo principal
Análisis → Propuesta → Aprobación → Envío

### Variantes
- Pedido automático.
- Pedido semiautomático.

### Beneficio aportado
Ahorro operativo.

### Prioridad
Should Have

## Analítica

### Objetivo
Optimizar decisiones.

### Descripción
Dashboards y análisis de consumo.

### Flujo principal
Captura → Procesado → Visualización

### Beneficio aportado
Control y optimización.

### Prioridad
Should Have

# 13. Casos de Uso

## CU-01 Registrar Inventario

### Nombre
Registrar inventario inicial

### Actor principal
Responsable del restaurante

### Actores secundarios
Gerente

### Objetivo
Registrar el stock disponible al inicio de la operación.

### Precondiciones
- Catálogo de productos creado.
- Usuario autenticado.

### Flujo principal
1. Accede al módulo de inventario.
2. Selecciona los productos.
3. Introduce cantidades.
4. Valida la información.
5. Guarda el inventario.

### Flujos alternativos
- Importación masiva mediante fichero.
- Copia de inventario previo.

### Excepciones
- Producto inexistente.
- Cantidades inválidas.

### Resultado esperado
Inventario registrado correctamente.

---

## CU-02 Registrar Venta

### Nombre
Actualizar inventario tras una venta

### Actor principal
Sistema TPV

### Actores secundarios
Motor de inventario

### Objetivo
Mantener el stock actualizado automáticamente.

### Precondiciones
- Integración TPV activa.
- Receta asociada al plato.

### Flujo principal
1. El TPV registra una venta.
2. Envía la operación al sistema.
3. El sistema identifica la receta.
4. Calcula el consumo.
5. Descuenta ingredientes.
6. Recalcula disponibilidad.

### Flujos alternativos
- Venta agrupada.
- Sincronización diferida.

### Excepciones
- Receta inexistente.
- Error de integración.

### Resultado esperado
Inventario actualizado en tiempo real.

---

## CU-03 Consultar Disponibilidad

### Nombre
Consultar disponibilidad de platos

### Actor principal
Camarero

### Actores secundarios
Sistema

### Objetivo
Conocer qué platos pueden venderse.

### Precondiciones
- Inventario actualizado.

### Flujo principal
1. Accede al catálogo.
2. Consulta disponibilidad.
3. Visualiza platos disponibles.

### Flujos alternativos
- Consulta desde TPV.
- Consulta desde dispositivo móvil.

### Excepciones
- Sistema no disponible.

### Resultado esperado
Disponibilidad mostrada correctamente.

---

## CU-04 Generar Pedido

### Nombre
Generar pedido de reposición

### Actor principal
Responsable de compras

### Actores secundarios
Proveedor

### Objetivo
Reponer existencias necesarias.

### Precondiciones
- Proveedores configurados.
- Umbrales definidos.

### Flujo principal
1. Sistema detecta stock bajo.
2. Genera sugerencia.
3. Usuario revisa.
4. Aprueba pedido.
5. Se envía al proveedor.

### Flujos alternativos
- Edición del pedido.
- Pedido manual.

### Excepciones
- Proveedor no disponible.

### Resultado esperado
Pedido emitido correctamente.

---

# 14. User Story Mapping

## Actividad: Administrar Inventario

### Tarea: Consultar existencias

#### US-001
Como responsable del restaurante  
Quiero consultar el stock actual  
Para conocer la disponibilidad real

- Valor: Muy alto
- Prioridad: Alta
- MVP

#### US-002
Como gerente  
Quiero visualizar niveles de inventario  
Para supervisar la operación

- Valor: Alto
- Prioridad: Alta
- MVP

### Tarea: Registrar movimientos

#### US-003
Como responsable del restaurante  
Quiero registrar entradas de mercancía  
Para mantener actualizado el stock

- Valor: Alto
- Prioridad: Alta
- MVP

#### US-004
Como responsable del restaurante  
Quiero registrar ajustes de inventario  
Para corregir discrepancias

- Valor: Alto
- Prioridad: Alta
- MVP

---

## Actividad: Gestionar Recetas

### Tarea: Crear y mantener recetas

#### US-005
Como responsable del restaurante  
Quiero configurar recetas  
Para automatizar el consumo de ingredientes

- Valor: Muy alto
- Prioridad: Alta
- MVP

#### US-006
Como responsable del restaurante  
Quiero actualizar recetas existentes  
Para reflejar cambios operativos

- Valor: Alto
- Prioridad: Media
- MVP

---

## Actividad: Procesar Ventas

### Tarea: Sincronizar ventas

#### US-007
Como sistema  
Quiero recibir ventas desde el TPV  
Para mantener el stock actualizado

- Valor: Muy alto
- Prioridad: Alta
- MVP

#### US-008
Como sistema  
Quiero descontar ingredientes automáticamente  
Para reflejar consumos reales

- Valor: Muy alto
- Prioridad: Alta
- MVP

---

## Actividad: Gestionar Compras

### Tarea: Detectar necesidades

#### US-009
Como responsable de compras  
Quiero recibir alertas de reposición  
Para evitar roturas de stock

- Valor: Muy alto
- Prioridad: Alta
- MVP

### Tarea: Automatizar pedidos

#### US-010
Como responsable de compras  
Quiero generar pedidos sugeridos  
Para reducir trabajo manual

- Valor: Alto
- Prioridad: Media
- Post-MVP

#### US-011
Como responsable de compras  
Quiero automatizar pedidos recurrentes  
Para optimizar reposiciones

- Valor: Alto
- Prioridad: Media
- Post-MVP

---

## Actividad: Analizar Operación

### Tarea: Consultar indicadores

#### US-012
Como gerente  
Quiero visualizar KPIs operativos  
Para tomar decisiones basadas en datos

- Valor: Muy alto
- Prioridad: Media
- Post-MVP

#### US-013
Como gerente  
Quiero analizar tendencias de consumo  
Para optimizar compras futuras

- Valor: Alto
- Prioridad: Media
- Post-MVP

---

# 15. Historias de Usuario Detalladas

## US-001 Consultar Stock

### Descripción
Permite visualizar el inventario actualizado.

### Criterios de aceptación
- Mostrar cantidad actual.
- Permitir búsqueda.
- Mostrar umbral mínimo.
- Mostrar última actualización.

### Reglas de negocio
- Datos actualizados en tiempo real.

### Casos límite
- Producto sin movimientos.
- Producto con stock cero.

### Dependencias
RF-001

### Prioridad
Alta

### Complejidad estimada
Media

---

## US-005 Gestionar Recetas

### Descripción
Permite definir ingredientes y cantidades por plato.

### Criterios de aceptación
- Crear receta.
- Modificar receta.
- Asociar ingredientes.
- Definir cantidades.

### Reglas de negocio
- Todo plato debe disponer de receta.

### Casos límite
- Ingrediente inexistente.
- Cantidad cero.

### Dependencias
RF-002

### Prioridad
Alta

### Complejidad estimada
Media

---

## US-008 Descuento Automático

### Descripción
Actualización automática del stock tras cada venta.

### Criterios de aceptación
- Identificar receta.
- Calcular consumo.
- Actualizar inventario.
- Registrar trazabilidad.

### Reglas de negocio
- El cálculo se realiza por ingredientes.

### Casos límite
- Receta incompleta.
- Venta duplicada.

### Dependencias
RF-002, RF-003

### Prioridad
Alta

### Complejidad estimada
Alta

---

## US-010 Pedido Sugerido

### Descripción
Genera recomendaciones automáticas de compra.

### Criterios de aceptación
- Analizar stock actual.
- Considerar mínimos.
- Generar propuesta.

### Reglas de negocio
- El usuario debe aprobar el pedido.

### Casos límite
- Sin proveedor asociado.

### Dependencias
RF-006, RF-008

### Prioridad
Media

### Complejidad estimada
Media

---

# 16. Requisitos No Funcionales

## Rendimiento

- Actualización de stock inferior a 5 segundos.
- Consulta de inventario inferior a 2 segundos.
- Dashboard operativo inferior a 3 segundos.

## Escalabilidad

- Soporte para múltiples restaurantes.
- Capacidad para gestionar miles de productos.
- Escalado horizontal de servicios.

## Seguridad

- Autenticación.
- Autorización basada en roles.
- MFA opcional.
- Cifrado TLS.
- Cifrado de datos sensibles.

## Disponibilidad

- Disponibilidad mínima del 99,9%.

## Fiabilidad

- Integridad transaccional.
- Recuperación ante fallos.

## Observabilidad

- Logging centralizado.
- Métricas operativas.
- Alertas automáticas.

## Trazabilidad

- Registro completo de movimientos.
- Seguimiento de cambios.

## Auditoría

- Historial de usuarios.
- Historial de inventario.
- Historial de recetas.

## Accesibilidad

- Cumplimiento WCAG 2.1 AA.

## Compatibilidad

- Chrome.
- Edge.
- Firefox.
- Safari.

## Mantenibilidad

- Arquitectura modular.
- Código documentado.
- APIs versionadas.

## Internacionalización

- Multiidioma.
- Configuración de zona horaria.
- Configuración de unidades.

## Protección de datos

- Cumplimiento RGPD.
- Gestión de consentimientos.
- Políticas de retención.

---

# 17. Reglas de Negocio

## RN-001

### Nombre
Consumo basado en receta

### Descripción
Toda venta genera consumo de ingredientes según receta.

### Justificación
Garantizar precisión.

### Impacto
Crítico.

---

## RN-002

### Nombre
Disponibilidad automática

### Descripción
Un plato no estará disponible cuando algún ingrediente crítico no alcance la cantidad necesaria.

### Justificación
Evitar ventas imposibles.

### Impacto
Alto.

---

## RN-003

### Nombre
Alerta de stock mínimo

### Descripción
Generar alertas al alcanzar umbrales configurables.

### Justificación
Reducir roturas.

### Impacto
Alto.

---

## RN-004

### Nombre
Validación de inventario inicial

### Descripción
Todo inventario inicial debe ser validado.

### Justificación
Evitar errores de origen.

### Impacto
Alto.

---

## RN-005

### Nombre
Aprobación de pedidos

### Descripción
Los pedidos sugeridos requieren aprobación humana.

### Justificación
Evitar compras incorrectas.

### Impacto
Medio.

---

## RN-006

### Nombre
Trazabilidad obligatoria

### Descripción
Toda modificación de inventario debe quedar registrada.

### Justificación
Auditoría.

### Impacto
Alto.

---

# 18. Arquitectura Conceptual

## Componentes principales

- Portal Web.
- Motor de Inventario.
- Motor de Recetas.
- Motor de Compras.
- Motor Analítico.
- Motor de Alertas.
- Servicio de Integración TPV.
- Servicio de Notificaciones.

## Sistemas involucrados

### Internos
- Plataforma principal.
- Base de datos operativa.
- Sistema analítico.

### Externos
- TPV.
- Proveedores.
- Servicios de correo electrónico.

## Integraciones

### TPV
Recepción de ventas y devoluciones.

### Proveedores
Generación y envío de pedidos.

### Servicios de comunicación
Envío de alertas y notificaciones.

## Flujos de información

1. Venta registrada en TPV.
2. Recepción del evento.
3. Consulta de receta.
4. Cálculo de consumo.
5. Actualización inventario.
6. Revisión de mínimos.
7. Generación de alertas.
8. Actualización de indicadores.

## Dependencias externas

- APIs TPV.
- Servicios email.
- Infraestructura cloud.

## Consideraciones técnicas

- APIs REST.
- Arquitectura desacoplada.
- Procesamiento asíncrono de eventos.
- Observabilidad integrada.

---

# 19. Riesgos

## Riesgos de Negocio

### R-001 Inventario inicial incorrecto

- Probabilidad: Alta
- Impacto: Alto
- Mitigación: Auditoría inicial.

### R-002 Baja adopción

- Probabilidad: Media
- Impacto: Alto
- Mitigación: Formación y acompañamiento.

---

## Riesgos de Producto

### R-003 Recetas mal configuradas

- Probabilidad: Media
- Impacto: Alto
- Mitigación: Validaciones y revisiones.

### R-004 Umbrales incorrectos

- Probabilidad: Media
- Impacto: Medio
- Mitigación: Configuración guiada.

---

## Riesgos Tecnológicos

### R-005 Fallo de integración TPV

- Probabilidad: Media
- Impacto: Muy Alto
- Mitigación: Reintentos y monitorización.

### R-006 Latencia elevada

- Probabilidad: Baja
- Impacto: Alto
- Mitigación: Arquitectura optimizada.

---

## Riesgos Operativos

### R-007 Errores de recepción

- Probabilidad: Media
- Impacto: Medio
- Mitigación: Validaciones obligatorias.

---

## Riesgos de Adopción

### R-008 Resistencia al cambio

- Probabilidad: Media
- Impacto: Medio
- Mitigación: Plan de gestión del cambio.

---

# 20. Roadmap Inicial

## MVP

### Objetivo
Validar la propuesta de valor principal.

### Incluye
- Inventario.
- Recetas.
- Integración TPV.
- Descuento automático.
- Disponibilidad de platos.
- Alertas de reposición.

### Justificación
Permite resolver el problema principal identificado.

---

## Versión 1

### Incluye
- Gestión de proveedores.
- Pedidos sugeridos.
- Dashboard ejecutivo.
- Auditoría completa.

### Justificación
Profundiza en la eficiencia operativa.

---

## Versión 2

### Incluye
- Forecast de demanda.
- Automatización avanzada.
- Reposición inteligente.
- Informes predictivos.

### Justificación
Mejora capacidades analíticas.

---

## Evolución Futura

- IA predictiva.
- Optimización automática de compras.
- Gestión multi-almacén.
- Gestión multi-restaurante.
- Integraciones con delivery.
- Benchmarking sectorial.

---

# 21. Lanzamiento y Adopción

## Estrategia de despliegue

### Fase 1
Piloto controlado.

### Fase 2
Despliegue progresivo.

### Fase 3
Escalado general.

---

## Estrategia de onboarding

- Asistente inicial.
- Importación guiada.
- Configuración paso a paso.

---

## Formación necesaria

### Responsable del restaurante
- Inventario.
- Recetas.

### Responsable de compras
- Alertas.
- Pedidos.

### Gerente
- Dashboards.
- KPIs.

### Camareros
- Disponibilidad de platos.

---

## Gestión del cambio

- Sponsor ejecutivo.
- Formación práctica.
- Soporte especializado.
- Seguimiento de adopción.

---

## Comunicación

- Comunicación previa.
- Materiales formativos.
- Sesiones de preguntas y respuestas.
- Canal de soporte.

---

# 22. Preguntas Abiertas

1. ¿Qué TPVs deben integrarse inicialmente?
2. ¿Cuál será el modelo comercial?
3. ¿El producto será multiempresa desde el MVP?
4. ¿Se requiere aplicación móvil?
5. ¿Habrá soporte offline?
6. ¿Cómo se enviarán los pedidos a proveedores?
7. ¿Qué nivel de automatización tendrán los pedidos?
8. ¿Existirá gestión multi-almacén?
9. ¿Se integrarán plataformas de delivery?
10. ¿Cómo se gestionarán sustituciones de ingredientes?
11. ¿Se permitirá stock negativo?
12. ¿Se registrarán mermas?
13. ¿Se gestionarán lotes y caducidades?
14. ¿Qué informes necesitan los gerentes?
15. ¿Qué SLA serán necesarios para clientes?

---

# 23. Anexos

## Glosario

| Término | Definición |
|----------|------------|
| Inventario | Existencias disponibles de un producto |
| Stock | Cantidad disponible de un producto |
| Receta | Relación de ingredientes necesarios para elaborar un plato |
| Reposición | Proceso de reabastecimiento |
| Merma | Pérdida de producto no vendida |
| Disponibilidad | Capacidad de ofrecer un plato para venta |

---

## Acrónimos

| Acrónimo | Significado |
|-----------|-------------|
| PRD | Product Requirements Document |
| TPV | Terminal Punto de Venta |
| KPI | Key Performance Indicator |
| MVP | Minimum Viable Product |
| API | Application Programming Interface |
| NPS | Net Promoter Score |
| CSAT | Customer Satisfaction Score |
| SLA | Service Level Agreement |
| RGPD | Reglamento General de Protección de Datos |

---

## Supuestos

1. El producto será SaaS.
2. Existirá integración con TPV.
3. Las recetas representan el consumo real.
4. Los usuarios disponen de conexión a internet.
5. La operativa principal será web.
6. Se gestionará al menos un almacén por restaurante.
7. El inventario será actualizado mediante eventos de venta.

---

## Referencias extraídas del análisis

### Problema

- Falta de visibilidad del stock.
- Roturas de stock inesperadas.
- Compras reactivas.
- Disponibilidad incorrecta.
- Escasa capacidad analítica.

### Oportunidad

- Integración de inventario, recetas, ventas y compras.
- Actualización en tiempo real.
- Automatización de reposiciones.
- Automatización de pedidos.
- Mejora de la toma de decisiones.

### Usuarios identificados

- Responsable del restaurante.
- Responsable de compras.
- Gerente.
- Camarero.
- Cliente.

### Hipótesis

- La automatización reducirá errores.
- Las alertas disminuirán roturas.
- La integración TPV mejorará la operación.
- La analítica optimizará las compras.

### Métricas

- Reducción de roturas de stock.
- Precisión del inventario.
- Tiempo de reposición.
- Reducción del trabajo manual.
- Número de pedidos automatizados.

### Riesgos

- Recetas incorrectas.
- Ventas no sincronizadas.
- Inventario inicial erróneo.
- Dependencia de integraciones TPV.
