import csv

def write_to_csv(data):
    with open("contact_tracing.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def search_csv_by_name(name):
    with open("contact_tracing.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == name:
                return row
    return None
