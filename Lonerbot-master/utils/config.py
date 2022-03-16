import json

def config():
    try:
        with open("config.json") as data:
            return json.load(data)
    except Exception as e:
        print("Error while loading config file: " + str(e))
        