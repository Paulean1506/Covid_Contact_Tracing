import tkinter as tk
from tkinter import ttk, messagebox
from csv_operations import CSVOperations

class SearchEntryWindow:
    def __init__(self, root, search_name):
        self.root = root
        self.search_name = search_name

    def search_entry(self, search_name):  # Accept search_name as an argument here
        if not search_name:
            messagebox.showerror("Error", "Please enter a name to search.")
            return

        # Read and search the CSV file for the name
        with open("contact_tracing.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == search_name:
                    messagebox.showinfo("Contact Information",
                                        f"Name: {row[0]}\nPhone Number: {row[1]}\nAddress: {row[2]}\nDate Visited: {row[3]}\n"
                                        f"\nTravelled outside country: {'Yes' if int(row[4]) == 1 else 'No'}\nTravel Information: {row[5]}\n"
                                        f"\nIn Quarantine: {'Quarantine Order (QO)' if int(row[6]) == 1 else 'Leave of Absence (LOA)' if int(row[6]) == 2 else 'Stay-home Notice (SHN)' if int(row[6]) == 3 else 'None of the above'}\n"
                                        f"\nContact with PUI: {'Yes' if int(row[7]) == 1 else 'No'}\nContact Information:\n {row[8]}\n"
                                        f"Fever: {'Yes' if int(row[9]) == 1 else 'No'}\nCough: {'Yes' if int(row[10]) == 1 else 'No'}\n"
                                        f"Sore Throat: {'Yes' if int(row[11]) == 1 else 'No'}\nRunny Nose: {'Yes' if int(row[12]) == 1 else 'No'}\n"
                                        f"Persistent Pain in the Chest: {'Yes' if int(row[13]) == 1 else 'No'}\nShortness of Breath: {'Yes' if int(row[14]) == 1 else 'No'}\n"
                                        f"\nWorking from Home: {'Yes' if int(row[15]) == 1 else 'No'}")
                    return

            messagebox.showinfo("Not Found", "Contact information not found.")