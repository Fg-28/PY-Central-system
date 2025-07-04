import tkinter as tk
from tkinter import messagebox
import time

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# First message
messagebox.showerror("Error", "Scheduled System Maintenance in Progress.")

# Wait 5 seconds
time.sleep(1)

# Second message
messagebox.showerror("Error", "Estimated Downtime: 08:30 TM-india, kolkata.\nWe appreciate your patience.")

time.sleep(1)
messagebox.showerror("Error", "We will get back to you when server is ready.")


# Optional: Exit
root.destroy()
