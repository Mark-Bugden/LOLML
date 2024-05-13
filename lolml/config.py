from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PATCHES_DIR = DATA_DIR / "patches" 

API_KEY_PATH = PROJECT_ROOT / "api_key.txt"

CONFIG_PATCH = "14.8.1"
