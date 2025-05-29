from model.product import Product

class Stock:

    @staticmethod
    def get_stock():
        return [
            {
                "product": Product("001", "Camiseta", 29.90),
                "quantity": 100
            },
            {
                "product": Product("002", "Calça Jeans", 89.90),
                "quantity": 50
            },
            {
                "product": Product("003", "Tênis Esportivo", 199.90),
                "quantity": 30
            },
            {
                "product": Product("004", "Jaqueta de Couro", 299.90),
                "quantity": 20
            },
            {
                "product": Product("005", "Relógio de Pulso", 499.90),
                "quantity": 10
            }
        ]