import tkinter as tk
from tkinter import ttk

# Adding custom style
def set_custom_style():
    style = ttk.Style()
    style.configure("Accent.TLabelframe", foreground="blue", background="white", font=("Helvetica", 12))
