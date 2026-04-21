import json
import time
import os

class ExperienceLoggerV1:
    def __init__(self, log_file="a7do_log.json"):
        self.log_file = log_file

        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump([], f)

    def log(self, data):
        entry = {
            "timestamp": time.time(),
            "data": data
        }

        with open(self.log_file, "r+") as f:
            logs = json.load(f)
            logs.append(entry)
            f.seek(0)
            json.dump(logs, f, indent=2)

    def get_recent(self, n=10):
        with open(self.log_file, "r") as f:
            logs = json.load(f)
        return logs[-n:]
