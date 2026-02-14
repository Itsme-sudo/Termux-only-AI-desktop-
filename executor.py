import os
import subprocess
from config import SYSTEM, IS_TERMUX

# PyAutoGUI not used in Termux
pyautogui = None

def open_app(app_name):
    if IS_TERMUX:
        # Use termux-open for apps/files
        subprocess.run(["termux-open", app_name])
    elif SYSTEM == "windows":
        try:
            subprocess.Popen([app_name])
        except FileNotFoundError:
            print(f"[Error] Could not open {app_name}")
    else:
        try:
            subprocess.Popen(["xdg-open", app_name])
        except FileNotFoundError:
            print(f"[Error] Could not open {app_name}")

def type_text(text):
    if IS_TERMUX:
        subprocess.run(["input", "text", text])
    else:
        print(f"[Typing fallback] {text}")

def search_file(filename, start_dir="."):
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None
