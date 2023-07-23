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

        # Basic Information Frame
        basic_info_frame = ttk.LabelFrame(self.add_entry_frame, text="Basic Information")
        basic_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Labels and Entry widgets
        label_name = ttk.Label(basic_info_frame, text="Name:")
        label_phone = ttk.Label(basic_info_frame, text="Phone:")
        label_address = ttk.Label(basic_info_frame, text="Address:")
        label_date_visited = ttk.Label(basic_info_frame, text="Date Visited:")

        # Prefix self. to make these instance attributes
        self.entry_name = ttk.Entry(basic_info_frame)
        self.entry_phone = ttk.Entry(basic_info_frame)
        self.entry_address = ttk.Entry(basic_info_frame)
        self.entry_date_visited = ttk.Entry(basic_info_frame)

        # Grid layout for basic information
        label_name.grid(row=0, column=0, sticky="w")
        label_phone.grid(row=1, column=0, sticky="w")
        label_address.grid(row=2, column=0, sticky="w")
        label_date_visited.grid(row=3, column=0, sticky="w")
        self.entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.entry_address.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_date_visited.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Add style for basic_info_frame
        basic_info_frame.configure(style="Accent.TLabelframe")