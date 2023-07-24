# csv_operations.py
import csv

def read_entries_from_csv(file_path):
    entries = []
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            entries.append(row)
    return entries

def write_entries_to_csv(file_path, entries):
    with open(file_path, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(entries)
