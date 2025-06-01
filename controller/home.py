from view.sale import SaleView
from controller.sale import SaleController

from view.product import ProductView
from controller.product import ProductController

from view.client import ClientView
from controller.client import ClientController

class HomeController:

    def __init__(self, view):
        self.view = view

        self.add_events()

    def add_events(self):
        self.view.get_sales_button().configure(command=self.open_sales_view)
        self.view.get_products_button().configure(command=self.open_products_view)
        self.view.get_clients_button().configure(command=self.open_clients_view)

    def open_sales_view(self):

        sales_view = SaleView(self.view)
        sales_controller = SaleController(sales_view)
        sales_controller.add_events()

        sales_view.mainloop()

    def open_products_view(self):

        products_view = ProductView(self.view)
        products_controller = ProductController(products_view)
        products_controller.add_events()

        products_view.mainloop()

    def open_clients_view(self):

        clients_view = ClientView(self.view)
        clients_controller = ClientController(clients_view)
        clients_controller.add_events()

        clients_view.mainloop()


