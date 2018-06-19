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

def save_and_close_json(data, identificator):
    json_name = "quests\\" + identificator + ".json"
    with open(json_name, 'w') as file:
        json.dump(data, file)

def is_done(data):
    return data["done"]

def set_done(data):
    data["done"] = True
    return data