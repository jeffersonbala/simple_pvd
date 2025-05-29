import sv_ttk
import tkinter as tk

from tkinter import ttk as ttk

from view.base import BaseView

class HomeView(BaseView):

    def __init__(self):
        super().__init__()

        self.create_widgets()

        self.visible = True

    def create_widgets(self):

        icon_label = ttk.Label(self, text="🛒", font=("Source Code Mono", 64))
        icon_label.pack(pady=20)

        title_label = ttk.Label(self, text="Bem Vindo ao Simple PDV!", font=("Source Code Mono", 32))
        title_label.pack(pady=20)

        exit_button = ttk.Button(self, text="Sair", command=self.quit)
        exit_button.pack(pady=10)

        sv_ttk.set_theme("dark")
