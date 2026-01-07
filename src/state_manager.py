import json
import os
from pathlib import Path

STATE_DIR = Path.home() / ".cligoblin"
STATE_FILE = STATE_DIR / "state.json"

def ensure_state_dir():
    if not STATE_DIR.exists():
        STATE_DIR.mkdir(parents=True)

def load_state():
    ensure_state_dir()
    if not STATE_FILE.exists():
        return None
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_state(state):
    ensure_state_dir()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)
