class Product:

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"