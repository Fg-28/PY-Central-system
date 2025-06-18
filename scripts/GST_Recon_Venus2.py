import tkinter as tk
from tkinter import messagebox
import time

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# First message
messagebox.showerror("Error", "Server Side Error, Server Crash...")

# Wait 5 seconds
time.sleep(5)

# Second message
messagebox.showerror("Error", "104 Missing Repo, Libraries.., Need them to run Application")

# Final message
messagebox.showerror("Critical", "Critical error... stopping script...")

# Optional: Exit
root.destroy()
