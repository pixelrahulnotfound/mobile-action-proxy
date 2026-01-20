import json
from mitmproxy import http

STATE_FILE = "proxy/state.json"
OUTPUT_FILE = "output/sessions/run_001.json"

session = {}

def load_action():
    with open(STATE_FILE) as f:
        return json.load(f).get("current_action")

def request(flow: http.HTTPFlow):
    action = load_action()
    if not action:
        return

    session.setdefault(action, []).append({
        "method": flow.request.method,
        "url": flow.request.pretty_url,
        "headers": dict(flow.request.headers),
        "body": flow.request.text
    })

    with open(OUTPUT_FILE, "w") as f:
        json.dump(session, f, indent=2)
