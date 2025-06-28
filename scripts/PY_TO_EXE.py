import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

def select_py_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        py_entry.delete(0, tk.END)
        py_entry.insert(0, filepath)

def select_output_folder():
    folderpath = filedialog.askdirectory()
    if folderpath:
        out_entry.delete(0, tk.END)
        out_entry.insert(0, folderpath)

def convert_to_exe():
    py_path = py_entry.get()
    out_folder = out_entry.get()
    exe_name = name_entry.get()

    if not os.path.isfile(py_path):
        messagebox.showerror("Error", "Invalid Python file path.")
        return
    if not os.path.isdir(out_folder):
        messagebox.showerror("Error", "Invalid output directory.")
        return
    if not exe_name:
        messagebox.showerror("Error", "Please provide a name for the .exe file.")
        return

    cmd = [
        "pyinstaller",
        "--onefile",
        "--distpath", out_folder,
        "--name", exe_name,
        py_path
    ]

    try:
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", f"EXE created at {out_folder}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Conversion Failed", f"Error: {e}")

# GUI setup
root = tk.Tk()
root.title("Py to EXE Converter")
root.geometry("500x200")

tk.Label(root, text="Python File:").pack()
py_entry = tk.Entry(root, width=60)
py_entry.pack()
tk.Button(root, text="Browse", command=select_py_file).pack()

tk.Label(root, text="Output Folder:").pack()
out_entry = tk.Entry(root, width=60)
out_entry.pack()
tk.Button(root, text="Browse", command=select_output_folder).pack()

tk.Label(root, text="EXE Name (without .exe):").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Button(root, text="Convert to EXE", command=convert_to_exe, bg="green", fg="white").pack(pady=10)

root.mainloop()
