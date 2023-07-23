import csv

def write_to_csv(data):
    with open("contact_tracing.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
