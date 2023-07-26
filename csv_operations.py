import csv

# Read and search the CSV file for the name
class CSVOperations:
    @staticmethod
    def read_csv_data():
        entries = []
        with open("contact_tracing.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                entries.append(row)
        return entries

    # Write all data back to the CSV file
    @staticmethod
    def write_csv_data(entries):
        with open("contact_tracing.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(entries)
