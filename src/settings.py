import json

def load_file(filename):
    with open(filename, "r") as f:
        return json.load(f)