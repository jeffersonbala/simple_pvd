from view.product import ProductView

class ProductController:

    def __init__(self, view):
        self.view : ProductView = view

    def add_events(self):
        self.view.get_save_product_button().configure(command=self.add_product)

    def add_product(self):
        print(self.view.get_form_data())

        