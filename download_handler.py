import logging
from watchdog.events import FileSystemEventHandler
from file_checker import is_file_stable
from manual_organizer import organize_folder
from config_handler import load_or_reset_config
from pathlib import Path
# ========== Event Handler ==========

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, folder_to_organize):
        self.folder_to_organize = folder_to_organize

    def handle_file(self, file_path):
        logging.info(f"📄 New file detected: {file_path}")
        if is_file_stable(file_path):
            logging.info(f"✅ File is stable. Organizing folder...")
            organize_folder(self.folder_to_organize)
        else:
            logging.warning(f"⏳ File not stable after checks: {file_path}")

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_extension = Path(file_path).suffix.lower()

            if file_extension in ['.crdownload', '.part', '.tmp']:
                logging.info(f"🕒 Temporary file detected, ignoring: {file_path}")
                return

            self.handle_file(file_path)

    def on_moved(self, event):
        if not event.is_directory:
            dest_path = event.dest_path
            logging.info(f"📁 File renamed/moved to: {dest_path}")
            self.handle_file(dest_path)
