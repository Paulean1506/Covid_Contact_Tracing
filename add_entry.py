import tkinter as tk
from tkinter import ttk, messagebox
import csv
from PIL import Image, ImageTk

class AddEntryWindow:
    def __init__(self, root, parent_app):
        self.root = root
        self.parent_app = parent_app
        self.add_entry_toplevel = tk.Toplevel(self.root)
        self.add_entry_toplevel.title("Add Entry")

        # Create a canvas to add scrollbars
        canvas = tk.Canvas(self.add_entry_toplevel, bg="#f0f0f0")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.add_entry_toplevel, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to place widgets
        self.add_entry_frame = ttk.Frame(canvas, style="Custom.TFrame")
        canvas.create_window((0, 0), window=self.add_entry_frame, anchor='nw')

        def go_back():
            self.add_entry_toplevel.destroy()

        # Define the new custom style for the information frames with the image background
        self.add_entry_frame_style = ttk.Style()
        image = Image.open("C:/Users/Paulean/Downloads/Blue and Red Online Medical Talk Youtube Thumbnail.jpg")
        self.photo = ImageTk.PhotoImage(image)
        self.add_entry_frame_style.element_create("Custom.TFrame.background", "image", self.photo)
        self.add_entry_frame_style.layout("Custom.TFrame", [('Custom.TFrame.border', {'sticky': 'nswe', 'children': [('Custom.TFrame.background', {'sticky': 'nswe'})]})])
        self.add_entry_frame_style.configure("Custom.TFrame")


        # Basic Information Frame
        basic_info_frame = ttk.LabelFrame(self.add_entry_frame, text="Basic Information", style="Accent.TLabelframe")
        basic_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Labels and Entry widgets
        label_name = ttk.Label(basic_info_frame, text="Name:", font=("Helvetica", 12))
        label_phone = ttk.Label(basic_info_frame, text="Phone:", font=("Helvetica", 12))
        label_address = ttk.Label(basic_info_frame, text="Address:", font=("Helvetica", 12))
        label_date_visited = ttk.Label(basic_info_frame, text="Date Visited:", font=("Helvetica", 12))

        # Prefix self. to make these instance attributes
        self.entry_name = ttk.Entry(basic_info_frame, font=("Helvetica", 12))
        self.entry_phone = ttk.Entry(basic_info_frame, font=("Helvetica", 12))
        self.entry_address = ttk.Entry(basic_info_frame, font=("Helvetica", 12))
        self.entry_date_visited = ttk.Entry(basic_info_frame, font=("Helvetica", 12))

        # Grid layout for basic information
        label_name.grid(row=0, column=0, sticky="w")
        label_phone.grid(row=1, column=0, sticky="w")
        label_address.grid(row=2, column=0, sticky="w")
        label_date_visited.grid(row=3, column=0, sticky="w")
        self.entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.entry_address.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_date_visited.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Travel Information Frame
        travel_info_frame = ttk.LabelFrame(self.add_entry_frame, text="Travel Information", style="Accent.TLabelframe")
        travel_info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for travel
        self.checkbox_travel = tk.IntVar()
        travel_label = tk.Label(travel_info_frame, text="Have you travelled to and from any country(ies) within the last 14 days?", font=("Helvetica", 12))
        travel_yes_checkbox = tk.Checkbutton(travel_info_frame, text="Yes", variable=self.checkbox_travel, onvalue=1, offvalue=0, font=("Helvetica", 12))
        travel_no_checkbox = tk.Checkbutton(travel_info_frame, text="No", variable=self.checkbox_travel, onvalue=0, offvalue=1, font=("Helvetica", 12))

        # Additional Information for travel
        travel_info_label = tk.Label(travel_info_frame, text="Country, State, City (If yes, please state the country(ies) you had visited):", font=("Helvetica", 12))
        self.travel_info_entry = tk.Entry(travel_info_frame, font=("Helvetica", 12))

        # Grid layout for travel information
        travel_label.grid(row=0, column=0, columnspan=2, sticky="w")
        travel_yes_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        travel_no_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        travel_info_label.grid(row=2, column=0, columnspan=2, sticky="w")
        self.travel_info_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Add style for travel_info_frame
        travel_info_frame.configure(style="Accent.TLabelframe")

        # Quarantine Information Frame
        quarantine_info_frame = ttk.LabelFrame(self.add_entry_frame, text="Quarantine Information", style="Accent.TLabelframe")
        quarantine_info_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for quarantine
        self.checkbox_quarantine = tk.IntVar()
        quarantine_label = tk.Label(quarantine_info_frame, text="Are you currently serving Quarantine Order (QO) / Leave of Absence (LOA) / Stay-home Notice (SHN)?", font=("Helvetica", 12))
        quarantine_qo_checkbox = tk.Checkbutton(quarantine_info_frame, text="Quarantine Order (QO)", variable=self.checkbox_quarantine, onvalue=1, offvalue=0, font=("Helvetica", 12))
        quarantine_loa_checkbox = tk.Checkbutton(quarantine_info_frame, text="Leave of Absence (LOA)", variable=self.checkbox_quarantine, onvalue=2, offvalue=0, font=("Helvetica", 12))
        quarantine_shn_checkbox = tk.Checkbutton(quarantine_info_frame, text="Stay-home Notice (SHN)", variable=self.checkbox_quarantine, onvalue=3, offvalue=0, font=("Helvetica", 12))
        quarantine_none_checkbox = tk.Checkbutton(quarantine_info_frame, text="None of the above", variable=self.checkbox_quarantine, onvalue=0, offvalue=4, font=("Helvetica", 12))

        # Grid layout for quarantine information
        quarantine_label.grid(row=0, column=0, columnspan=2, sticky="w")
        quarantine_qo_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        quarantine_loa_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        quarantine_shn_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        quarantine_none_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Contact Information Frame
        contact_info_frame = ttk.LabelFrame(self.add_entry_frame, text="Contact Information", style="Accent.TLabelframe")
        contact_info_frame.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for contact
        self.checkbox_contact = tk.IntVar()
        contact_label = tk.Label(contact_info_frame, text="Have you been in contact with any COVID-19 confirmed infected/diagnosed or suspected person(s), or any person(s) under Quarantine Order (QO) / Leave of Absence (LOA) / Stay-home Notice (SHN)?", font=("Helvetica", 12))
        contact_yes_checkbox = tk.Checkbutton(contact_info_frame, text="Yes", variable=self.checkbox_contact, onvalue=1, offvalue=0, font=("Helvetica", 12))
        contact_no_checkbox = tk.Checkbutton(contact_info_frame, text="No", variable=self.checkbox_contact, onvalue=0, offvalue=1, font=("Helvetica", 12))

        # Additional Information for contact
        contact_info_label = tk.Label(contact_info_frame, text="Stranger / dd-mm-yyyy (If yes, please tell us your relationship with the people and your last contact date with them if no type N/A):", font=("Helvetica", 12))
        self.contact_info_entry = tk.Entry(contact_info_frame, font=("Helvetica", 12))

        # Grid layout for contact information
        contact_label.grid(row=0, column=0, columnspan=2, sticky="w")
        contact_yes_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        contact_no_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        contact_info_label.grid(row=2, column=0, columnspan=2, sticky="w")
        self.contact_info_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Health Information Frame
        health_info_frame = ttk.LabelFrame(self.add_entry_frame, text="Health Information", style="Accent.TLabelframe")
        health_info_frame.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for health
        self.checkbox_fever = tk.IntVar()
        self.checkbox_cough = tk.IntVar()
        self.checkbox_sore_throat = tk.IntVar()
        self.checkbox_runny_nose = tk.IntVar()
        self.checkbox_persistent_pain = tk.IntVar()
        self.checkbox_shortness_breath = tk.IntVar()

        health_label = tk.Label(health_info_frame, text="Please state whether you've experienced/are experiencing the following:", font=("Helvetica", 12))

        health_fever_checkbox = tk.Checkbutton(health_info_frame, text="Fever", variable=self.checkbox_fever, onvalue=1, offvalue=0, font=("Helvetica", 12))
        health_cough_checkbox = tk.Checkbutton(health_info_frame, text="Cough", variable=self.checkbox_cough, onvalue=1, offvalue=0, font=("Helvetica", 12))
        health_sore_throat_checkbox = tk.Checkbutton(health_info_frame, text="Sore Throat", variable=self.checkbox_sore_throat, onvalue=1, offvalue=0, font=("Helvetica", 12))
        health_runny_nose_checkbox = tk.Checkbutton(health_info_frame, text="Runny Nose", variable=self.checkbox_runny_nose, onvalue=1, offvalue=0, font=("Helvetica", 12))
        health_persistent_pain_checkbox = tk.Checkbutton(health_info_frame, text="Persistent Pain in the Chest", variable=self.checkbox_persistent_pain, onvalue=1, offvalue=0, font=("Helvetica", 12))
        health_shortness_breath_checkbox = tk.Checkbutton(health_info_frame, text="Shortness of Breath", variable=self.checkbox_shortness_breath, onvalue=1, offvalue=0, font=("Helvetica", 12))

        # Grid layout for health information
        health_label.grid(row=0, column=0, columnspan=2, sticky="w")
        health_fever_checkbox.grid(row=1, column=0, sticky="w")
        health_cough_checkbox.grid(row=2, column=0, sticky="w")
        health_sore_throat_checkbox.grid(row=3, column=0, sticky="w")
        health_runny_nose_checkbox.grid(row=4, column=0, sticky="w")
        health_persistent_pain_checkbox.grid(row=5, column=0, sticky="w")
        health_shortness_breath_checkbox.grid(row=6, column=0, sticky="w")

        # Working From Home Frame
        working_from_home_frame = ttk.LabelFrame(self.add_entry_frame, text="Working From Home", style="Accent.TLabelframe")
        working_from_home_frame.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Checkboxes for working from home
        self.checkbox_working_from_home = tk.IntVar()
        working_from_home_label = tk.Label(working_from_home_frame, text="Are you working from home now?", font=("Helvetica", 12))
        working_from_home_yes_checkbox = tk.Checkbutton(working_from_home_frame, text="Yes", variable=self.checkbox_working_from_home, onvalue=1, offvalue=0, font=("Helvetica", 12))
        working_from_home_no_checkbox = tk.Checkbutton(working_from_home_frame, text="No", variable=self.checkbox_working_from_home, onvalue=0, offvalue=1, font=("Helvetica", 12))

        # Grid layout for working from home information
        working_from_home_label.grid(row=0, column=0, columnspan=2, sticky="w")
        working_from_home_yes_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        working_from_home_no_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Button to Add Entry
        button_add = ttk.Button(self.add_entry_frame, text="Add", command=self.add_entry, style="Accent.TButton")
        button_back = ttk.Button(self.add_entry_frame, text="Back", command=go_back, style="Accent.TButton")

        # Grid layout for buttons
        button_add.grid(row=6, column=0, columnspan=2, pady=5, sticky="w")
        button_back.grid(row=6, column=0, columnspan=2, pady=5, sticky="e")

    def add_entry(self):
        # Validate if all fields are filled
        if not self.entry_name.get() or not self.entry_phone.get() or not self.entry_address.get() or not self.entry_date_visited.get():
            messagebox.showerror("Error", "Please fill all fields.")
            return

        # Read all existing data from the CSV file into a list of lists
        entries = []
        with open("contact_tracing.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                entries.append(row)

        # Add the new entry to the list
        new_entry = [
            self.entry_name.get(), self.entry_phone.get(), self.entry_address.get(), self.entry_date_visited.get(),
            self.checkbox_travel.get(), self.travel_info_entry.get(),
            self.checkbox_quarantine.get(),
            self.checkbox_contact.get(), self.contact_info_entry.get(),
            self.checkbox_fever.get(), self.checkbox_cough.get(), self.checkbox_sore_throat.get(),
            self.checkbox_runny_nose.get(), self.checkbox_persistent_pain.get(), self.checkbox_shortness_breath.get(),
            self.checkbox_working_from_home.get()
        ]
        entries.append(new_entry)

        # Write all data back to the CSV file
        with open("contact_tracing.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(entries)

        messagebox.showinfo("Success", "Contact information added successfully.")
        if self.add_entry_toplevel:  
            self.add_entry_toplevel.destroy()

    

