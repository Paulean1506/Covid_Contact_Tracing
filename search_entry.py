import tkinter as tk
from tkinter import ttk, messagebox
import csv
from csv_operations import search_csv_by_name
from styles import configure_custom_style

class SearchEntryWindow:
    def __init__(self, root, search_name):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        configure_custom_style()

        # Create a custom style
        style = ttk.Style()
        style.configure("Accent.TLabelframe", foreground="blue", background="white", font=("times new roman", 1))

        # Labels
        self.label_search = ttk.Label(root, text="Search by Name:")
        self.label_search.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Entry widget
        self.entry_search = ttk.Entry(root)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Button
        self.button_search = ttk.Button(root, text="Search", command=self.search_entry)
        self.button_search.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
