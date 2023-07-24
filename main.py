import tkinter as tk
import tkinter.ttk as ttk
from add_entry import AddEntryWindow
from search_entry import SearchEntryWindow

class ContactTracingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        self.add_entry_toplevel = None