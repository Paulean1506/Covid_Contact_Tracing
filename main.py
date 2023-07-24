import tkinter as tk
import tkinter.ttk as ttk
from add_entry import AddEntryWindow
from search_entry import SearchEntryWindow

class ContactTracingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.add_entry_toplevel = None

        # Create a custom style
        style = ttk.Style()
        style.configure("Accent.TLabelframe", foreground="blue", background="white", font=("Helvetica", 12))

        # Labels
        self.label_search = ttk.Label(root, text="Search by Name:")
        self.label_app_title = ttk.Label(root, text="COVID Contact Tracing App", font=("Helvetica", 16, "bold"))

        # Entry widget
        self.entry_search = ttk.Entry(root)

        # Buttons
        self.button_add_entry = ttk.Button(root, text="Add Entry", command=self.add_entry_window)
        self.button_search = ttk.Button(root, text="Search Entry", command=self.search_entry)

        # Layout using grid geometry manager
        self.label_app_title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.label_search.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_search.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.button_add_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.button_search.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    def add_entry_window(self):
        self.add_entry_toplevel = tk.Toplevel(self.root)  # Use self.add_entry_toplevel
        self.add_entry_toplevel.title("Add Entry")
        add_entry_window = AddEntryWindow(self.add_entry_toplevel)

    def search_entry(self):
        search_name = self.entry_search.get()  # Get the value from the entry widget
        search_entry_window = SearchEntryWindow(self.root, search_name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactTracingApp(root)
    root.mainloop()
