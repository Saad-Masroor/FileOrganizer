import os
import shutil
from pathlib import Path
import logging
# Categories of files to be organized
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html"],
    "Datasets": [".csv", ".json"],
    "Others": []
}

def organize_folder(folder_path):
    p = Path(folder_path)

    for file in p.iterdir():
        if file.is_file():
            # Ignore .tmp files
            if file.suffix.lower() == ".tmp":
                continue

            moved = False
            for category, extensions in CATEGORIES.items():
                if file.suffix.lower() in [ext.lower() for ext in extensions]:
                    category_folder = p / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(category_folder / file.name))
                    logging.info(f"Moved '{file.name}' to '{category_folder.name}'")
                    moved = True
                    break

            if not moved:
                # Move files with no matching category
                others_folder = p / "Others"
                others_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(others_folder / file.name))

if __name__ == "__main__":
    folder_to_organize = input("Enet the path of the folder to oraganize: ")
    organize_folder(folder_to_organize)
    print(f"Files in '{folder_to_organize}' have been organized.")
    
    
