import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from csv_operations import write_to_csv
from styles import configure_custom_style

class AddEntryWindow:
    def __init__(self, add_entry_toplevel):
        self.add_entry_toplevel = add_entry_toplevel
        self.add_entry_toplevel.title("Add Entry")

        