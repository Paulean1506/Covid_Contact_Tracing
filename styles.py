# styles.py
import tkinter.ttk as ttk

def configure_custom_style():
    style = ttk.Style()
    style.configure("Accent.TLabelframe", foreground="blue", background="white", font=("Helvetica", 12))
