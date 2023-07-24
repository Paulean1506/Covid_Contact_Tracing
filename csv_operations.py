import csv

class CSVOperations:
    @staticmethod
    def read_csv_data():
        entries = []
        with open("contact_tracing.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                entries.append(row)
        return entries

    @staticmethod
    def write_csv_data(entries):
        with open("contact_tracing.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(entries)
