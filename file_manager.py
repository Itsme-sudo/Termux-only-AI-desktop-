import os
from config import DATA_DIR

LOG_FILE = os.path.join(DATA_DIR, "ai_log.txt")

def save_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def read_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return f.readlines()
