import json
import datetime

_CONFIG_PATH = "./config.json"

def _getversion():
    try:
        with open(_CONFIG_PATH, "r") as file:
            version = json.load(file)["version"]
    except Exception:
        version = "unknown"
    return version

def export(path = "./file.json", **kwargs):
    metadata = {}
    
    metadata["time"] = str(datetime.datetime.now())
    metadata["version"] = _getversion()

    kwargs["metadata"] = metadata
    
    try:
        with open(path, "w") as file:
            json.dump(kwargs, file)
        return True
    except Exception:
        return False

def import_(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
        return data
    except Exception:
        return False

if __name__ == "__main__":
    export(path="./file.json",
           name="NAME",
           description="DESCRIPTION",
           genres=["GENRE1", "GENRE2"], 
           media_type="TV",
           episodes=12,
           year=2024,
           studios=["STUDIO1", "STUDIO2"],
           rating="R")
    data = import_(path="./file.json")
    print(data)
    
