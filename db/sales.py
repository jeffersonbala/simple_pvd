from .loader import Loader

class Sales:

    @staticmethod
    def get_sales(self):
        return Loader.file_loader(self.path)