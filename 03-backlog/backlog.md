# Épica 1: Gestión de inventario

## HU-01 - Alta de productos de inventario

**Como** responsable del restaurante  
**Quiero** registrar ingredientes, bebidas y otros productos almacenados  
**Para** poder controlar su stock dentro del sistema.

### Criterios de aceptación

**Escenario: Crear un producto correctamente**

```gherkin
Dado que soy un usuario autorizado
Cuando registro un producto indicando nombre, unidad de medida, stock inicial,
stock mínimo, stock óptimo y proveedor habitual
Entonces el sistema guarda el producto
Y el producto queda disponible en el inventario.
```

**Escenario: Campos obligatorios**

```gherkin
Dado que estoy creando un producto
Cuando dejo vacío el nombre o la unidad de medida
Entonces el sistema informa del error
Y no permite guardar el producto.
```

**Escenario: Error al crear un producto**

```gherkin
Dado que soy un usuario sin autorizacion para crear productos
Cuando registro un producto indicando nombre, unidad de medida, stock inicial,
stock mínimo, stock óptimo y proveedor habitual
Entonces el sistema no guarda el producto
Y muestra un mensaje de error avisando de que el usuario no tiene permisos para crear productos.
```

---

## HU-02 - Modificar información de un producto

**Como** responsable del restaurante  
**Quiero** editar los datos de un producto  
**Para** mantener actualizada la información del inventario.

### Criterios de aceptación

```gherkin
Dado que existe un producto registrado
Cuando modifico cualquiera de sus datos
Entonces el sistema guarda los cambios
Y muestra la información actualizada.
```

---

## HU-03 - Consultar stock actual

**Como** responsable del restaurante  
**Quiero** visualizar el stock real de cada producto  
**Para** conocer el inventario disponible en cualquier momento.

### Criterios de aceptación

```gherkin
Dado que existen productos en inventario
Cuando consulto el listado de inventario
Entonces visualizo el stock actual de cada producto
Y su unidad de medida correspondiente.
```

---

## HU-04 - Registrar entradas de stock

**Como** responsable del restaurante  
**Quiero** registrar recepciones de mercancía  
**Para** actualizar el stock disponible.

### Criterios de aceptación

```gherkin
Dado que existe un producto en inventario
Cuando registro una entrada de stock de 20 unidades
Entonces el sistema incrementa el stock actual en 20 unidades
Y registra el movimiento realizado.
```

---

# Épica 2: Gestión de recetas

## HU-05 - Crear receta de un plato

**Como** gerente del restaurante  
**Quiero** asociar ingredientes y cantidades a un plato  
**Para** controlar el consumo real de ingredientes.

### Criterios de aceptación

```gherkin
Dado que existen productos registrados en inventario
Cuando creo una receta e indico los ingredientes y cantidades necesarias
Entonces el sistema guarda la receta
Y la asocia al plato correspondiente.
```

---

## HU-06 - Modificar receta

**Como** gerente del restaurante  
**Quiero** actualizar los ingredientes de un plato  
**Para** reflejar cambios en la elaboración.

### Criterios de aceptación

```gherkin
Dado que existe una receta
Cuando añado, elimino o modifico ingredientes
Entonces el sistema actualiza la receta
Y conserva la nueva composición del plato.
```

---

# Épica 3: Consumo y actualización automática de stock

## HU-07 - Descontar stock tras una venta

**Como** responsable del restaurante  
**Quiero** que el sistema descuente automáticamente los ingredientes consumidos  
**Para** disponer de un inventario actualizado en tiempo real.

### Criterios de aceptación

**Escenario: Venta de un plato**

```gherkin
Dado que existe una receta para el plato vendido
Y hay stock suficiente de sus ingredientes
Cuando se registra la venta del plato
Entonces el sistema descuenta automáticamente las cantidades correspondientes
Y actualiza el inventario en tiempo real.
```

**Escenario: Venta múltiple**

```gherkin
Dado que existe una receta para una hamburguesa
Cuando se venden 5 hamburguesas
Entonces el sistema descuenta el equivalente a 5 recetas
Y actualiza el stock resultante.
```

---

## HU-08 - Registrar movimientos de inventario

**Como** responsable del restaurante  
**Quiero** disponer de un histórico de movimientos  
**Para** auditar las variaciones de stock.

### Criterios de aceptación

```gherkin
Dado que se produce una entrada o salida de stock
Cuando el movimiento es registrado
Entonces el sistema almacena fecha, producto, cantidad y motivo
Y permite su posterior consulta.
```

---

# Épica 4: Alertas de reposición

## HU-09 - Generar alerta por stock mínimo

**Como** responsable del restaurante  
**Quiero** recibir alertas cuando un producto alcance su stock mínimo  
**Para** evitar roturas de stock.

### Criterios de aceptación

```gherkin
Dado que un producto tiene definido un stock mínimo
Cuando su stock actual es igual o inferior a dicho valor
Entonces el sistema genera una alerta de reposición.
```

---

## HU-10 - Sugerir cantidad de reposición

**Como** responsable del restaurante  
**Quiero** que el sistema sugiera cuánto pedir  
**Para** recuperar el stock óptimo.

### Criterios de aceptación

```gherkin
Dado que un producto ha alcanzado el stock mínimo
Cuando se genera la alerta
Entonces el sistema calcula la diferencia entre stock actual y stock óptimo
Y propone dicha cantidad como reposición recomendada.
```

---

## HU-11 - Notificar alertas al responsable

**Como** responsable del restaurante  
**Quiero** recibir una notificación automática  
**Para** conocer rápidamente incidencias de inventario.

### Criterios de aceptación

```gherkin
Dado que existe una alerta de reposición
Cuando el sistema detecta la incidencia
Entonces envía una notificación al responsable
Y marca el producto como pendiente de reposición.
```

---

# Épica 5: Gestión de pedidos a proveedores

## HU-12 - Generar borradores de pedidos

**Como** responsable de compras  
**Quiero** generar automáticamente borradores de pedido  
**Para** agilizar las reposiciones.

### Criterios de aceptación

```gherkin
Dado que existen productos pendientes de reposición
Cuando solicito generar pedidos
Entonces el sistema crea un borrador para cada proveedor afectado.
```

---

## HU-13 - Agrupar productos por proveedor

**Como** responsable de compras  
**Quiero** que los productos se agrupen por proveedor  
**Para** reducir trabajo administrativo.

### Criterios de aceptación

```gherkin
Dado que varios productos requieren reposición
Cuando se genera el pedido
Entonces el sistema agrupa los artículos por proveedor habitual.
```

---

## HU-14 - Enviar pedidos por correo electrónico

**Como** responsable de compras  
**Quiero** enviar pedidos directamente desde el sistema  
**Para** acelerar la comunicación con los proveedores.

### Criterios de aceptación

```gherkin
Dado que existe un pedido en estado borrador
Cuando selecciono la opción enviar
Entonces el sistema remite el pedido por correo electrónico
Y registra la fecha de envío.
```

---

# Épica 6: Disponibilidad de platos

## HU-15 - Calcular disponibilidad de platos

**Como** gerente del restaurante  
**Quiero** conocer qué platos pueden prepararse  
**Para** evitar ofrecer productos no disponibles.

### Criterios de aceptación

```gherkin
Dado que existen recetas asociadas a los platos
Cuando el sistema evalúa el inventario
Entonces determina qué platos son disponibles
Y cuáles no son disponibles.
```

---

## HU-16 - Marcar automáticamente platos no disponibles

**Como** camarero  
**Quiero** visualizar qué platos están agotados  
**Para** no ofrecerlos a los clientes.

### Criterios de aceptación

```gherkin
Dado que falta algún ingrediente obligatorio de una receta
Cuando se consulta la carta
Entonces el plato aparece marcado como NO DISPONIBLE.
```

---

## HU-17 - Actualizar disponibilidad en tiempo real

**Como** gerente del restaurante  
**Quiero** que la disponibilidad se actualice automáticamente  
**Para** reflejar el estado real del inventario.

### Criterios de aceptación

```gherkin
Dado que se produce una venta o reposición
Cuando cambia el stock de un ingrediente
Entonces el sistema recalcula automáticamente la disponibilidad de los platos afectados.
```

---

# Épica 7: Integración con TPV y carta digital

## HU-18 - Reflejar disponibilidad en TPV

**Como** camarero  
**Quiero** que el TPV muestre únicamente productos disponibles  
**Para** evitar errores durante la toma de pedidos.

### Criterios de aceptación

```gherkin
Dado que existen platos no disponibles
Cuando se consulta el TPV
Entonces dichos platos aparecen deshabilitados o identificados claramente.
```

---

## HU-19 - Actualizar carta digital

**Como** cliente del restaurante  
**Quiero** visualizar únicamente productos disponibles  
**Para** evitar pedidos imposibles de servir.

### Criterios de aceptación

```gherkin
Dado que cambia la disponibilidad de un plato
Cuando se actualiza el inventario
Entonces la carta digital refleja el nuevo estado automáticamente.
```

---

# Épica 8: Dashboard y analítica

## HU-20 - Visualizar productos con stock crítico

**Como** gerente  
**Quiero** ver los productos con stock crítico en un panel  
**Para** tomar decisiones rápidamente.

### Criterios de aceptación

```gherkin
Dado que existen productos con stock igual o inferior al mínimo
Cuando accedo al dashboard
Entonces visualizo un listado de productos críticos.
```

---

## HU-21 - Consultar productos agotados

**Como** gerente  
**Quiero** ver los productos agotados  
**Para** priorizar su reposición.

### Criterios de aceptación

```gherkin
Dado que existen productos con stock igual a cero
Cuando accedo al dashboard
Entonces visualizo los productos agotados.
```

---

## HU-22 - Consultar pedidos pendientes

**Como** gerente  
**Quiero** visualizar pedidos pendientes de recepción  
**Para** controlar futuras entradas de stock.

### Criterios de aceptación

```gherkin
Dado que existen pedidos emitidos no recepcionados
Cuando consulto el dashboard
Entonces visualizo el listado de pedidos pendientes.
```

---

## HU-23 - Consultar consumo diario

**Como** gerente  
**Quiero** analizar el consumo diario de productos  
**Para** entender los patrones de uso.

### Criterios de aceptación

```gherkin
Dado que existen ventas registradas
Cuando consulto el dashboard
Entonces visualizo el consumo acumulado por día.
```

---

## HU-24 - Consultar productos más consumidos

**Como** gerente  
**Quiero** identificar los productos más consumidos  
**Para** optimizar compras y previsiones.

### Criterios de aceptación

```gherkin
Dado que existen datos históricos de consumo
Cuando consulto el dashboard
Entonces el sistema muestra un ranking de productos más consumidos.
```

---

## HU-25 - Previsión de agotamiento

**Como** gerente  
**Quiero** conocer cuándo se agotará un producto según su ritmo de consumo  
**Para** anticipar pedidos.

### Criterios de aceptación

```gherkin
Dado que existe histórico suficiente de consumo
Cuando consulto un producto
Entonces el sistema muestra una fecha estimada de agotamiento
Y el cálculo se basa en el consumo medio registrado.
```

# MVP recomendado

1. HU-01 Alta de productos.
2. HU-03 Consulta de stock.
3. HU-05 Gestión de recetas.
4. HU-07 Descuento automático de stock.
5. HU-09 Alertas de reposición.
6. HU-10 Sugerencia de reposición.
7. HU-15 Cálculo de disponibilidad de platos.
8. HU-16 Marcar platos no disponibles.
9. HU-20 Dashboard de stock crítico.
