class Product:

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"
    
    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "price": self.price
        }