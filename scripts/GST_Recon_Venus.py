import tkinter as tk
from tkinter import messagebox
import time

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Step 1: Info message
messagebox.showwarning("Notice", "Scheduled System Maintenance in Progress.")

# Wait 1 second
time.sleep(1)

# Step 2: Warning message
messagebox.showwarning("Downtime Alert", "Estimated Downtime: 08:30 TM-India, Kolkata.\nWe appreciate your patience.")

# Wait 1 second
time.sleep(1)
messagebox.showinfo("Error", "We will get back to you when server is ready.")


# Optional: Exit
root.destroy()
