import json
from pathlib import Path

if not Path("config.json").exists() or Path("config.json").stat().st_size == 0:
    with Path("config.json").open("w") as f:
        json.dump({
            "DB_file" : "database.csv",
            "log_file" : "log.txt"
        }, f)

with Path("config.json").open("r") as f:
    a = json.load(f)

DB_file = a["DB_file"]
log_file = a["log_file"]
