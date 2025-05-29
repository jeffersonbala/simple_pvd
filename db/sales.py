class Sales:

    @staticmethod
    def get_sales(self):
        return [
            {
                "client": None,
                "date": "2023-10-01T12:00:00",
                "items": [
                    {
                        "product": {
                            "code": "P001",
                            "name": "Product 1",
                            "price": 10.0
                        },
                        "quantity": 2
                    },
                    {
                        "product": {
                            "code": "P002",
                            "name": "Product 2",
                            "price": 20.0
                        },
                        "quantity": 1
                    }
                ],
            }
        ]