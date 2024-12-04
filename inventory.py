# inventory.py
class InventoryItem:
    def __init__(self, item_id, name, quantity, price, supplier):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    def __repr__(self):
        return f"InventoryItem({self.item_id}, {self.name}, {self.quantity}, {self.price}, {self.supplier})"

    def total_value(self):
        return self.quantity * self.price
