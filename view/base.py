import os
import sv_ttk
import tkinter as tk

from PIL import Image

class BaseView(tk.Tk):

    def __init__(self):
        super().__init__()

        sv_ttk.set_theme("dark", self)

        self.title("Simple PDV System")
        self.geometry("800x600")
        self.visible = True

    def image_loader(self, path: str, width=32, height=32) -> Image.Image:
        try:
            img = Image.open(path)
            return img.resize((width, height))
        except tk.TclError as e:
            print(f"Error loading image from {path}: {e}")
            return None
        
    def toggle_visibility(self):
        print(f"Visibility on {type(self)}, before was {self.visible}, now toggling to {not self.visible}")
        if self.visible:
            self.withdraw()
            return
        self.deiconify()

    def create_temp_label(self, text: str, parent=None, temp=7000):
        if not parent:
            parent = self
        label = tk.Label(parent, text=text, foreground='red')
        label.pack(pady=10)
        label.after(temp, label.destroy)  


    