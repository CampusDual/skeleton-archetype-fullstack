# Especificación Funcional

## Nombre

Gestión Inteligente de Inventario para Restauración

---

# Objetivo

Proporcionar una plataforma capaz de gestionar inventario, recetas, reposiciones y disponibilidad de platos en tiempo real.

---

# Alcance

La solución incluye:

- Gestión de inventario.
- Gestión de recetas.
- Consumo automático.
- Alertas.
- Compras.
- Disponibilidad.
- Integración TPV.
- Dashboard analítico.

---

# Requisitos Funcionales

1. Gestión de inventario:
   El sistema debe permitir:

   - Alta de productos.
   - Edición de productos.
   - Consulta de stock.
   - Registro de entradas.
   - Registro de movimientos.

    Datos del producto:

   - Nombre.
   - Unidad de medida.
   - Stock inicial.
   - Stock mínimo.
   - Stock óptimo.
   - Proveedor habitual.

2. Gestión de recetas:
   El sistema debe permitir:

   - Crear recetas.
   - Editar recetas.
   - Asociar ingredientes a platos.
   - Definir cantidades por ingrediente.

3. Consumo automático:
   Tras cada venta:

   - Obtener receta asociada.
   - Calcular ingredientes consumidos.
   - Descontar stock.
   - Registrar movimiento.

4. Alertas:
   El sistema debe:

   - Detectar stock mínimo.
   - Generar alertas.
   - Calcular reposición recomendada.
   - Notificar responsables.

5. Compras:
   El sistema debe:

   - Generar borradores.
   - Agrupar por proveedor.
   - Permitir envío por correo.

6. Disponibilidad:
   El sistema debe:

   - Calcular disponibilidad de platos.
   - Marcar platos agotados.
   - Recalcular automáticamente.

7. Integración TPV:
   El sistema debe:
   
   - Sincronizar ventas con el inventario.
   - Actualizar stock automáticamente tras cada transacción.

8. Dashboard analítico:
   Dashboard con:

   - Stock crítico.
   - Productos agotados.
   - Pedidos pendientes.
   - Consumo diario.
   - Ranking de consumo.
   - Predicción de agotamiento.

# Requisitos no funcionales:

  - Actualización en tiempo real.
  - Auditoría de movimientos.
  - Escalabilidad.
  - Seguridad basada en roles.
  - Disponibilidad 24x7.

# MVP

RF-01
RF-02
RF-03
RF-04
RF-06
RF-08 (stock crítico)