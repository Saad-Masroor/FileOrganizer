from auto_organizer import start_auto_organizer
from logger_setup import setup_logging
from download_handler import DownloadHandler
from pathlib import Path
from watchdog.observers import Observer
import logging
from config_handler import load_or_reset_config

# ========== Load Config and Set up Logging ==========

config = load_or_reset_config()  # This will handle both config reset and loading
USE_EMOJIS = config.get("use_emojis", True)

def e(emoji, fallback=""):
    return emoji if USE_EMOJIS else fallback

setup_logging(config)

# ========== Start Auto Organizer ==========

def start_auto_organizer(folder_to_watch):
    # Initialize the event handler
    event_handler = DownloadHandler(folder_to_watch)

    # Set up the observer to watch the specified folder
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)

    try:
        observer.start()
        logging.info(f"🔍 Watching folder: {folder_to_watch}")
        print(f"🔍 Watching folder: {folder_to_watch}")
        while True:
            pass  # Keep the program running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# ========== Main Execution ==========

if __name__ == "__main__":
    # Folder to watch is fetched from the config
    folder_to_watch = config.get("watch_folder")
    start_auto_organizer(folder_to_watch)
