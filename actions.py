import json

STATE_FILE = "proxy/state.json"

def set_action(name):
    with open(STATE_FILE, "w") as f:
        json.dump({"current_action": name}, f)

def clear_action():
    with open(STATE_FILE, "w") as f:
        json.dump({"current_action": None}, f)
