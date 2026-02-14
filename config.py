import platform
import os

SYSTEM = platform.system().lower()  # 'windows', 'linux', 'darwin'
IS_TERMUX = os.path.exists("/data/data/com.termux/files/home")

HOME_DIR = os.path.expanduser("~")
DATA_DIR = os.path.join(HOME_DIR, ".local_ai_assistant")
os.makedirs(DATA_DIR, exist_ok=True)
