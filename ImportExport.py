import json
import datetime

_CONFIG_PATH = "./config.json"

def _GetVersion():
    try:
        with open(_CONFIG_PATH, "r") as file:
            version = json.load(file)["version"]
    except Exception:
        version = "unknown"
    return version

def Export(path = "./file.json", **kwargs):
    metadata = {}
    
    metadata["time"] = datetime.datetime.now()
    metadata["version"] = _GetVersion()

    kwargs["metadata"] = metadata

    try:
        with open(path, "w") as file:
            json.dump(file, kwargs)
        return True
    except Exception:
        return False

def Import(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
        return data
    except Exception:
        pass
    
