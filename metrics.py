import json
from datetime import datetime

METRICS_FILE = 'metrics.json'

def log_usage(prompt):
    try:
        with open(METRICS_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append({
        'timestamp': datetime.utcnow().isoformat(),
        'prompt_length': len(prompt)
    })

    with open(METRICS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
