import re

from .base import BaseView

from db.stock import Stock

from tkinter import ttk, Toplevel

class ProductView(BaseView):

    def __init__(self, parent: BaseView):
        super().__init__()

        self.create_widgets()

        self.parent = parent

        self.visible = True

    def create_widgets(self):

        icon_label = ttk.Label(self, text="🛍️ Produtos", font=("Source Code Mono", 64))
        icon_label.pack(pady=20)

        tabs = ttk.Notebook(self)
        tabs.pack(fill="both", expand=True)

        product_tab = ttk.Frame(tabs)
        tabs.add(product_tab, text="Produtos")
        self.create_table(Stock.get_stock(), parent=product_tab)

        new_product_tab = ttk.Frame(tabs)
        tabs.add(new_product_tab, text="Novo Produto")
        self.create_new_product_form(parent=new_product_tab)

        back_button = ttk.Button(self, text="Fechar", command=self.destroy)
        back_button.pack(side="right", padx=10, pady=10)

    
    def create_table(self, data, parent=None):

        if not parent:
            parent = self

        scrollbar = ttk.Scrollbar(parent, orient="vertical")
        table = ttk.Treeview(parent, columns=("Cod.", "Descrição", "Quantidade", "Preço"), show="headings", yscrollcommand=scrollbar.set)

        table.heading("Cod.", text="Cod.")
        table.heading("Descrição", text="Descrição")
        table.heading("Quantidade", text="Quantidade")
        table.heading("Preço", text="Preço")

        table.column("Cod.", width=20)
        table.column("Descrição", width=200)
        table.column("Quantidade", width=100)
        table.column("Preço", width=100)

        for item in data:
            table.insert("", "end", values=(
                item["product"].code,
                item["product"].name,
                item["quantity"],
                f"R$ {item['product'].price:.2f}"
            ))

        table.pack(fill="both", expand=True)

    def create_new_product_form(self, parent=None):
        if not parent:
            parent = self

        name_label = ttk.Label(parent, text="Nome:")
        name_label.pack(pady=5)
        self.name_entry = ttk.Entry(parent)
        self.name_entry.pack(pady=5)

        price_label = ttk.Label(parent, text="Preço:")
        price_label.pack(pady=5)
        self.price_entry = ttk.Entry(parent)
        self.price_entry.pack(pady=5)

        quantity_label = ttk.Label(parent, text="Quantidade:")
        quantity_label.pack(pady=5)
        self.quantity_entry = ttk.Entry(parent)
        self.quantity_entry.pack(pady=5)

        self.save_button = ttk.Button(parent, text="Salvar")
        self.save_button.pack(pady=10)

    def get_save_product_button(self) -> ttk.Button:
        return self.save_button
    
    def get_name_entry(self) -> ttk.Entry:
        return self.name_entry
    
    def get_price_entry(self) -> ttk.Entry:
        return self.price_entry
    
    def get_form_data(self) -> dict:
        name = self.get_name_entry().get()
        price = self.get_price_entry().get()
        quantity = self.quantity_entry.get() if hasattr(self, 'quantity_entry') else None

        if not quantity:
            quantity = 0

        if not name or not price:
            raise ValueError("Nome e preço são obrigatórios.")

        if not re.match(r"^\d+(\.\d{1,2})?$", price):
            raise ValueError("Preço deve ser um número válido.")

        return {
            "name": name,
            "price": float(price),
            "quantity": quantity
        }
        