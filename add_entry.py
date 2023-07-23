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

        # Travel Information Frame
        travel_info_frame = tk.LabelFrame(self.add_entry_frame, text="Travel Information")
        travel_info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for travel
        self.checkbox_travel = tk.IntVar()
        travel_label = tk.Label(travel_info_frame, text="Have you travelled to and from any country(ies) within the last 14 days?")
        travel_yes_checkbox = tk.Checkbutton(travel_info_frame, text="Yes", variable=self.checkbox_travel, onvalue=1, offvalue=0)
        travel_no_checkbox = tk.Checkbutton(travel_info_frame, text="No", variable=self.checkbox_travel, onvalue=0, offvalue=1)

        # Additional Information for travel
        travel_info_label = tk.Label(travel_info_frame, text="Country, State, City (If yes, please state the country(ies) you had visited):")
        self.travel_info_entry = tk.Entry(travel_info_frame)

        # Grid layout for travel information
        travel_label.grid(row=0, column=0, columnspan=2, sticky="w")
        travel_yes_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        travel_no_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        travel_info_label.grid(row=2, column=0, columnspan=2, sticky="w")
        self.travel_info_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Quarantine Information Frame
        quarantine_info_frame = tk.LabelFrame(self.add_entry_frame, text="Quarantine Information")
        quarantine_info_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for quarantine
        self.checkbox_quarantine = tk.IntVar()
        quarantine_label = tk.Label(quarantine_info_frame, text="Are you currently serving Quarantine Order (QO) / Leave of Absence (LOA) / Stay-home Notice (SHN)?")
        quarantine_qo_checkbox = tk.Checkbutton(quarantine_info_frame, text="Quarantine Order (QO)", variable=self.checkbox_quarantine, onvalue=1, offvalue=0)
        quarantine_loa_checkbox = tk.Checkbutton(quarantine_info_frame, text="Leave of Absence (LOA)", variable=self.checkbox_quarantine, onvalue=2, offvalue=0)
        quarantine_shn_checkbox = tk.Checkbutton(quarantine_info_frame, text="Stay-home Notice (SHN)", variable=self.checkbox_quarantine, onvalue=3, offvalue=0)
        quarantine_none_checkbox = tk.Checkbutton(quarantine_info_frame, text="None of the above", variable=self.checkbox_quarantine, onvalue=0, offvalue=4)

        # Grid layout for quarantine information
        quarantine_label.grid(row=0, column=0, columnspan=2, sticky="w")
        quarantine_qo_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        quarantine_loa_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        quarantine_shn_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        quarantine_none_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
