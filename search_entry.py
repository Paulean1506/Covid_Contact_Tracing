import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from csv_operations import search_csv_by_name
from styles import configure_custom_style

class SearchEntryWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        configure_custom_style()

        
