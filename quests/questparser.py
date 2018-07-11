class quest:
    def __init_(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.type = data["type"]
        self.phases = data["phases"]

        if self.type == "fight":
            self.enemyId = data["enemyId"]

