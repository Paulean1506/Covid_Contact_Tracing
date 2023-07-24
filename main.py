import tkinter as tk
from contact_tracing_app import ContactTracingApp
from styles import configure_custom_style

if __name__ == "__main__":
    root = tk.Tk()
    configure_custom_style()  # Call the function to configure the custom style
    app = ContactTracingApp(root)
    root.mainloop()
