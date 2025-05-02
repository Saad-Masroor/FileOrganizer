from watchdog.observers import Observer
from download_handler import DownloadHandler
import time
import os

def start_auto_organizer(path_to_watch):
    if not os.path.exists(path_to_watch):
        print(f"Path {path_to_watch} does not exist.")
        exit(1)

    event_handler = DownloadHandler(path_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()

    print(f"O.O Watching '{path_to_watch}' for new downloads... (Press Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nX.X Stopped watching.")

    observer.join()
