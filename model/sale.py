from datetime import datetime

class SaleItem:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.date = datetime.now()

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

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "client": self.client.to_dict() if self.client else None,
            "items": [item.to_dict() for item in self.items],
            "amount": self.amount
        }