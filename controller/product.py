import uuid

from view.product import ProductView
from model.product import Product

from db.stock import Stock

class ProductController:

    def __init__(self, view):
        self.view : ProductView = view

    def add_events(self):
        self.view.get_save_product_button().configure(command=self.add_product)

    def add_product(self):
        data = self.view.get_form_data()

        if data:
            product = Product(
                code=uuid.uuid1(),
                name=data['name'],
                price=float(data['price'])
            )

            print(f"Product created: {product}")


        Stock.include_register(product=product, quantity=data['quantity'])
        
        


        