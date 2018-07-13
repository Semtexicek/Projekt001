class quest:
    def __init__(self, data):
        self.data = data
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.type = data["type"]
        self.phases = data["phases"]

        if self.type == "fight":
            self.enemyId = data["enemyId"]

    def is_type_fight(self):
        if self.type == "fight":
            return True
        return False
