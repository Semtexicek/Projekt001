def is_doable(data):
    if data == -1:
        return False
    return True

def get_id(data):
    return data["id"]

def get_name(data):
    return data["name"]

def get_description(data):
    return data["description"]

def get_type(data):
    return data["type"]

def get_phases(data):
    return data["phases"]

def get_enemy(data):
    if data["type"] == "fight":
        return data["enemyId"]
    return None

