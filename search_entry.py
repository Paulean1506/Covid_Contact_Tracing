import tkinter as tk
from tkinter import ttk, messagebox
import csv
from csv_operations import CSVOperations

class SearchEntryWindow:
    def __init__(self, root, search_name):
        self.root = root
        self.search_name = search_name

    def search_entry(self):
        if not self.search_name:
            messagebox.showerror("Error", "Please enter a name to search.")
            return

        # Read and search the CSV file for the name
        try:
            with open("contact_tracing.csv", "r", newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 1 and row[0] == self.search_name:
                        messagebox.showinfo("Contact Information",
                                            f"Name: {row[0]}\nPhone Number: {row[1]}\nAddress: {row[2]}\nDate Visited: {row[3]}\n"
                                            # ... (rest of the formatted message) ...
                                            f"\nWorking from Home: {'Yes' if int(row[15]) == 1 else 'No'}")
                        return
        except FileNotFoundError:
            messagebox.showerror("Error", "Contact tracing data file not found.")
            return
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while searching: {str(e)}")
            return

        messagebox.showinfo("Not Found", "Contact information not found.")