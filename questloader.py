import json

def load_quest(identificator):
    data = open_json(identificator)

    if is_done(data):
        return -1

    return data

def open_json(identificator):
    json_name = "quests\\" + identificator + ".json"
    with open(json_name, 'r') as file:
        return json.load(file)

def is_done(data):
    return data["done"]