from pathlib import Path

########################
# Patch
########################
CONFIG_PATCH = "14.9.1"


########################
# Project directory paths
########################
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PATCHES_DIR = DATA_DIR / "patches"


########################
# API key location and rate limits
########################
API_KEY_PATH = PROJECT_ROOT / "api_key.txt"

# Increase ratelimit periods by 10% to account for desynchronous calculations
API_RATELIMIT = {"requests": 50, "period": 10 * 1.1}


########################
# Reference codes and information for tiers and queues
########################
HTTP_CODES = {
    400: "Bad request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Data not found",
    405: "Method not allowed",
    415: "Unsupported media type",
    429: "Rate limit exceeded",
    500: "Internal server error",
    502: "Bad gateway",
    503: "Service unavailable",
    504: "Gateway timeout",
}

TIERS = {
    "IRON": ["I", "II", "III", "IV"],
    "BRONZE": ["I", "II", "III", "IV"],
    "SILVER": ["I", "II", "III", "IV"],
    "GOLD": ["I", "II", "III", "IV"],
    "PLATINUM": ["I", "II", "III", "IV"],
    "EMERALD": ["I", "II", "III", "IV"],
    "DIAMOND": ["I", "II", "III", "IV"],
}

QUEUES = ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
