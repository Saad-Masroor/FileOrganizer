import time
from pathlib import Path

# ========== File Stability Checker ==========

def is_file_stable(file_path, attempts=5, delay=2):
    path = Path(file_path)
    for _ in range(attempts):
        if not path.exists():
            return False
        initial_size = path.stat().st_size
        time.sleep(delay)
        if not path.exists():
            return False
        if path.stat().st_size == initial_size:
            return True
    return False
