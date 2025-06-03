from .loader import Loader

from model.product import Product

class Stock:

    @staticmethod
    def get_stock(path):
        return Loader.file_loader(path)
    
    def include_register(self, product: Product, quantity: int):
        stock = Stock.get_stock()
        stock.append({
            "product": product,
            "quantity": quantity
        })
        return stock
    
    @staticmethod
    def count():
        return len(Stock.get_stock())