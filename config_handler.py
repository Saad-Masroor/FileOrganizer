import json
import sys
from pathlib import Path

# Handle base directory whether run as script or .exe
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

def load_or_reset_config():
    config_path = BASE_DIR / "config.json"

    if config_path.exists():
        reset_choice = input("Do you want to reset the config? (y/N): ").strip().lower()
        if reset_choice == 'y':
            config_path.unlink()
            print("✅ Config file deleted. Please provide new settings.")
            return create_or_load_config(config_path)
    else:
        print("No existing config found. Let's create a new one.")
    
    return create_or_load_config(config_path)

def create_or_load_config(config_path):
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        folder = input("Enter folder to watch (e.g., C:/Users/Name/Downloads): ").strip()
        config = {
            "watch_folder": folder,
            "use_emojis": True,
            "logging": {
                "log_to_file": True,
                "log_file_path": "file_watcher.log",
                "log_level": "INFO"
            }
        }
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        print("✅ Config file created.")

    return config
