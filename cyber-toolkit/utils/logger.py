import os
import json
from datetime import datetime


def save_log(tool, data):

    base = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    reports = os.path.join(base, "reports")
    os.makedirs(reports, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_path = os.path.join(reports, f"{tool}_{timestamp}.json")

    entry = {
        "tool": tool,
        "timestamp": timestamp,
        "data": data
    }

    # guardar archivo individual
    with open(file_path, "w") as f:
        json.dump(entry, f, indent=4)

    # guardar en historial global
    global_file = os.path.join(reports, "history.json")

    if os.path.exists(global_file):
        with open(global_file, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)

    with open(global_file, "w") as f:
        json.dump(history, f, indent=4)

    print(f"\n[LOG] Guardado en: {file_path}")