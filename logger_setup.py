import logging
import sys
from pathlib import Path

# Handle base directory whether script or .exe
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

def setup_logging(config):
    log_file = BASE_DIR / config["logging"]["log_file_path"]
    log_level = getattr(logging, config["logging"]["log_level"].upper(), logging.INFO)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
