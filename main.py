from flask import Flask, request, Response
from datetime import datetime
import os

app = Flask(__name__)
SCRIPTS_FOLDER = "scripts"

# Universal Python control block (with tkinter GUI for password input and F1 trigger)
UNIVERSAL_PYTHON_HEADER = r'''
import uuid
import requests
import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import datetime
import keyboard

def get_guid():
    return str(uuid.getnode())

def show_popup(title, message, type='info'):
    root = tk.Tk()
    root.withdraw()
    if type == 'info':
        messagebox.showinfo(title, message)
    elif type == 'error':
        messagebox.showerror(title, message)
    root.destroy()

def fetch_json(script_name, guid):
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    url = f"https://script.google.com/macros/s/AKfycby_QpaF75QTHhXWxpNPmjsnylyM_8RBDGIbHT3-FygJPGLs1kikJDEkufHHe18kJ1o7vg/exec?script={script_name}&guid={guid}&t={timestamp}"
    try:
        resp = requests.get(url)
        if not resp.text.strip().startswith("{"):
            show_popup("ERROR", "Invalid response received. Exiting.", "error")
            exit()
        return json.loads(resp.text)
    except Exception as e:
        show_popup("ERROR", f"Network error: {e}", "error")
        exit()

def main():
    script_name = "DYNAMIC"
    guid = get_guid()
    password = "FG@RL5851"

    root = tk.Tk()
    root.withdraw()
    entered = simpledialog.askstring("Authorization", "Enter system authorization code:", show="*")
    root.destroy()

    if entered != password:
        show_popup("AUTH FAILED", "Credentials Incorrect. Exiting Script...", "error")
        exit()

    data = fetch_json(script_name, guid)
    run = str(data.get("run", "false")).lower() == "true"
    shutdown = str(data.get("shutdown", "false")).lower() == "true"

    if shutdown:
        show_popup("Script Crashed...", "Critical Error. System Closing down in 3 seconds...", "error")
        os.system("shutdown /s /t 3")
        exit()

    if not run:
        show_popup("SYSTEM ERROR", "Script not authorised to run. Closing.", "error")
        exit()

    show_popup("SYSTEM LAUNCH", "SCRIPT running in 5 seconds...\nPress F1 to begin", "info")
    keyboard.wait("f1")
    # ===== CUSTOM LOGIC BELOW =====

if __name__ == "__main__":
    main()
'''

MISSING_SCRIPT_LOGIC = r'''
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
messagebox.showerror("SCRIPT ERROR", "The requested script was not found on the server.")
root.destroy()
exit()
'''

@app.route("/get_script")
def get_script():
    script_name = request.args.get("script", "").strip()
    guid = request.args.get("guid", "").strip()

    if not script_name:
        return Response("Missing script parameter", 400)

    script_path = os.path.join(SCRIPTS_FOLDER, f"{script_name}.py")

    print(f"[{datetime.utcnow()}] Script requested: {script_name} | GUID: {guid}")

    if os.path.isfile(script_path):
        with open(script_path, "r", encoding="utf-8") as f:
            logic = f.read()
    else:
        print(f"[{datetime.utcnow()}] WARNING: Script not found for {script_name}")
        logic = MISSING_SCRIPT_LOGIC

    combined = UNIVERSAL_PYTHON_HEADER.replace('script_name = \"DYNAMIC\"', f'script_name = \"{script_name}\"') + "\n\n" + logic
    return Response(combined, mimetype="text/plain")

@app.route("/")
def home():
    return "Python central dynamic script server is running."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
