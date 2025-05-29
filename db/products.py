class ProductsDB:

    @staticmethod
    def get_products():
        # TODO: carregar produtos de um CSV
        return [
            {
                "code": "001",
                "name": "Camiseta",
                "price": 29.90
            },
            {
                "code": "002",
                "name": "Calça Jeans",
                "price": 89.90
            },
            {
                "code": "003",
                "name": "Tênis Esportivo",
                "price": 199.90
            },
            {
                "code": "004",
                "name": "Jaqueta de Couro",
                "price": 299.90
            },
            {
                "code": "005",
                "name": "Relógio de Pulso",
                "price": 499.90
            }
        ]