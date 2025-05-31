from view.sale import SaleView
from controller.sale import SaleController
class HomeController:

    def __init__(self, view):
        self.view = view

        self.add_events()

    def add_events(self):
        self.view.get_sales_button().configure(command=self.open_sales_view)

    def open_sales_view(self):

        sales_view = SaleView(self.view)
        sales_controller = SaleController(sales_view)
        sales_controller.add_events()

        sales_view.mainloop()


