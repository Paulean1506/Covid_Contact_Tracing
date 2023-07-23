import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from csv_operations import write_to_csv
from styles import configure_custom_style

class AddEntryWindow:
    def __init__(self, add_entry_toplevel):
        self.add_entry_toplevel = add_entry_toplevel
        self.add_entry_toplevel.title("Add Entry")

        # Create a canvas to add scrollbars
        canvas = tk.Canvas(self.add_entry_toplevel)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.add_entry_toplevel, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to place widgets
        self.add_entry_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.add_entry_frame, anchor='nw')

        def go_back():
            self.add_entry_toplevel.destroy()