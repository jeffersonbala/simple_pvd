import pandas as pd
from .loader import Loader

from model.product import Product

class Stock:

    @staticmethod
    def get_stock(path="data/stock.json"):
        return Loader.file_loader(path)
    

    @staticmethod
    def include_register(product: Product, quantity: int):
        stock = Stock.get_stock()
        
        stock = pd.concat([stock, pd.DataFrame([{
            "code": product.code.hex,
            "name": product.name,
            "price": product.price,
            "quantity": quantity
        }])], ignore_index=True)

        stock.head

        Loader.update_file(stock, "stock")
        return stock
    
    @staticmethod
    def count(path="data/stock.json"):
        return len(Stock.get_stock(path))