# Design

## Domain Model

### Product

Represents an inventory item.

Attributes:

- id
- name
- unit
- currentStock
- minimumStock
- optimalStock
- supplier

### Recipe

Represents the ingredient composition of a dish.

### Dish

Commercial product sold to customers.

### InventoryMovement

Tracks stock changes.

### PurchaseOrder

Represents a supplier order.

### Alert

Represents stock warning conditions.

---

## Main Flows

### Inventory Update

Sale
→ Recipe
→ Stock Consumption
→ Inventory Update
→ Availability Recalculation

### Replenishment

Stock Below Minimum
→ Alert
→ Recommended Quantity
→ Draft Purchase Order

### Dish Availability

Inventory Change
→ Availability Calculation
→ POS Update
→ Digital Menu Update