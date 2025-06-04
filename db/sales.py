from .loader import Loader

class Sales:

    @staticmethod
    def get_sales(self):
        return Loader.file_loader(self.path)
    
    @staticmethod
    def include_register(self, data):
        sales = Sales.get_sales(self)
        sales.append(data)
        Loader.update_file(sales, "sales")
        return sales