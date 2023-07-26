# COVID Contact Tracing App with GUI

This is a COVID contact tracing application with a graphical user interface (GUI) written in Python using the Tkinter library. The application allows users to input typical information found in a COVID contact tracing app, writes the collected information to a CSV file, and provides functionalities to add and search for entries. It is designed to help users keep track of contact information and health status related to COVID-19.

## Files

- `main.py`: The main program that initializes the Tkinter GUI and starts the application.
- `contact_tracing_app.py`: Contains the `ContactTracingApp` class, which defines the main application window and its functionality.
- `add_entry.py`: Contains the `AddEntryWindow` class, which defines the window for adding new contact entries.
- `search_entry.py`: Contains the `SearchEntryWindow` class, which defines the window for searching contact entries.
- `csv_operations.py`: Contains the `CSVOperations` class for reading and writing data to a CSV file.
- `styles.py`: Contains functions to set custom styles for Tkinter widgets.

## Features

- Add new contact entries with basic information, travel information, quarantine status, contact details, health information, and working from home status.
- Search for contact entries based on the name.
- Data is saved in a CSV file (`contact_tracing.csv`) for easy management and retrieval.

## Usage

1. Run the application by executing the `main.py` file.
2. Click the "Add Entry" button to add a new contact entry with the required information.
3. Click the "Search Entry" button and enter a name to search for specific contact entries.

## Notes

- This application is intended for educational purposes and not for official contact tracing purposes.
- Please do not use downloaded programs for official contact tracing purposes.
- Do not follow any online contact tracing programming tutorials to maintain originality and creativity.
