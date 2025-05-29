import os
import tkinter as tk

from PIL import Image

class BaseView(tk.Tk):

    def __init__(self):
        super().__init__()
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

    