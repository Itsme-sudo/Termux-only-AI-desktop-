import re
from executor import open_app, type_text, search_file
from file_manager import save_log
from config import IS_TERMUX

def interpret_command(command):
    command = command.lower()

    # Rule-based AI (Termux-safe)
    open_match = re.search(r"open (\w+)", command)
    if open_match:
        app_name = open_match.group(1)
        open_app(app_name)
        save_log(f"Opened {app_name}")
        return f"Opening {app_name}"

    type_match = re.search(r"type (.+)", command)
    if type_match:
        text = type_match.group(1)
        type_text(text)
        save_log(f"Typed: {text}")
        return f"Typed: {text}"

    search_match = re.search(r"search file (.+)", command)
    if search_match:
        filename = search_match.group(1)
        path = search_file(filename)
        save_log(f"Searched for {filename}: {path}")
        return f"Found at: {path}" if path else "File not found"

    return "Command not recognized"
