import re
import subprocess
import os
from executor import open_app, type_text, search_file
from file_manager import save_log
from config import IS_TERMUX, SYSTEM

USE_ML = False

# Optional desktop AI using tiny model
if not IS_TERMUX:
    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM

        tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
        model = AutoModelForCausalLM.from_pretrained("distilgpt2")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        USE_ML = True
    except Exception as e:
        print(f"[ML fallback] {e}")

def ai_response(prompt):
    if USE_ML:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_length=50)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    return "ML not available."

def interpret_command(command):
    command = command.lower()

    # Open apps
    open_match = re.search(r"open (\w+)", command)
    if open_match:
        app_name = open_match.group(1)
        open_app(app_name)
        save_log(f"Opened {app_name}")
        return f"Opening {app_name}"

    # Type text
    type_match = re.search(r"type (.+)", command)
    if type_match:
        text = type_match.group(1)
        type_text(text)
        save_log(f"Typed: {text}")
        return f"Typed: {text}"

    # Search file
    search_match = re.search(r"search file (.+)", command)
    if search_match:
        filename = search_match.group(1)
        path = search_file(filename)
        save_log(f"Searched for {filename}: {path}")
        return f"Found at: {path}" if path else "File not found"

    # Battery status
    if "battery" in command:
        if IS_TERMUX:
            output = subprocess.getoutput("termux-battery-status")
            save_log(f"Battery: {output}")
            return output
        else:
            return "Battery info not available on this device."

    # List files in folder
    list_match = re.search(r"list files(?: in (.+))?", command)
    if list_match:
        folder = list_match.group(1) or "."
        if os.path.exists(folder):
            files = os.listdir(folder)
            return f"Files in {folder}: {', '.join(files)}"
        return f"Folder {folder} not found."

    # Screenshot (Termux)
    if "screenshot" in command:
        if IS_TERMUX:
            subprocess.run(["termux-screenshot", "-p", "screenshot.png"])
            return "Screenshot saved as screenshot.png"
        return "Screenshot not available on this device."

    # Ask AI fallback
    if "ask ai" in command:
        question = command.replace("ask ai", "").strip()
        return ai_response(question)

    return "Command not recognized"
