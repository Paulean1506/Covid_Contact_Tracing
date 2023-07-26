import tkinter as tk
from tkinter import ttk, messagebox
from add_entry import AddEntryWindow
from search_entry import SearchEntryWindow
from csv_operations import CSVOperations
from tkinter import PhotoImage
from PIL import Image, ImageTk
from styles import set_custom_style

class ContactTracingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.add_entry_toplevel = None

        # Set custom style
        set_custom_style()

        # Load the image using PIL (Pillow)
        self.background_image = Image.open("C:/Users/Paulean/Desktop/CALCULUS/GettyImages-1215392772.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image)

        # Set the background image on a label
        self.background_label = ttk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Create a Label widget to display the background image
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Header style
        header_style = ttk.Style()
        header_style.configure("Header.TLabel", font=("Helvetica", 20, "bold"), foreground="red")

        # Labels
        self.label_search = ttk.Label(root, text="Search by Name:", font=("Helvetica", 16, "bold"))
        self.label_app_title = ttk.Label(root, text="COVID Contact Tracing App", style="Header.TLabel")

        # Entry widget
        self.entry_search = ttk.Entry(root, font=("Helvetica", 12))

        # Buttons
        self.button_add_entry = ttk.Button(root, text="Add Entry", command=self.add_entry_window, style="Custom.TButton")
        self.button_search = ttk.Button(root, text="Search Entry", command=self.perform_search, style="Custom.TButton")  

        # Layout using grid geometry manager
        self.label_app_title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.label_search.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_search.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.button_add_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.button_search.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Set the background color of the main frame
        self.root.configure(bg="#f0f0f0")

        # Disable resizing of the window
        self.root.resizable(False, False)

    def add_entry_window(self):
        self.add_entry_toplevel = tk.Toplevel(self.root)  
        self.add_entry_toplevel.title("Add Entry")
        add_entry_window = AddEntryWindow(self.add_entry_toplevel, self)

    def search_entry(self):
        search_name = self.entry_search.get()  

        if not search_name:
            messagebox.showerror("Error", "Please enter a name to search.")
            return

        search_entry_window = SearchEntryWindow(self.root, search_name)

    def perform_search(self):
        search_name = self.entry_search.get()
        search_entry_window = SearchEntryWindow(self.root, search_name)
        search_entry_window.search_entry()

