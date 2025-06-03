from .loader import Loader

from model.product import Product

class ProductsDB:

    @staticmethod
    def get_products(path):
        stock_df = Loader.file_loader(path)

        products = stock_df["product"].apply(
            lambda x: Product(
                code=x["code"],
                name=x["name"],
                price=x["price"]
            )
        )

        return products.tolist()

    
    def include_register(self, data):
        product = Product(code=self.count() + 1, name=data["name"], price=data["price"])
        products = ProductsDB.get_products()
        products.append(product)
        return products