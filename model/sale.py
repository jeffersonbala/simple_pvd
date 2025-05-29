from datetime import datetime

class SaleItem:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return f"SaleItems(product={self.product}, quantity={self.quantity})"

class Sale:

    def __init__(self, client = None):
        self.date = datetime.now()
        self.client = client
        self.items = []

    @property
    def amount(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.items.append(SaleItem(product, quantity))

    def remove_item(self, product, quantity=None):
        for item in self.items:
            if item.product == product:
                if quantity is not None:
                    if item.quantity < quantity:
                        raise ValueError("Not enough quantity to remove.")
                    item.quantity -= quantity
                else:
                    self.items.remove(item)
                return
        raise ValueError("Product not found in sale items.")