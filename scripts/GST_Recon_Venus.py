import tkinter as tk
from tkinter import messagebox
import time

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# First message
messagebox.showerror("Error", "Scheduled System Maintenance in Progress.\nSome features may be temporarily unavailable.")

# Wait 5 seconds
time.sleep(1)

# Second message
messagebox.showerror("Error", "Estimated Downtime: 18:30 TM-india, kolkata.\nWe appreciate your patience.")



# Optional: Exit
root.destroy()
