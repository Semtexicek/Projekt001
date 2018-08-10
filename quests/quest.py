class Quest():
    def __init__(self, quest_json):
        self.data = quest_json
        self.data_id = self.data["id"]
        self.name = self.data["name"]
        self.description =  self.data["description"]
        self.type = self.data["type"]
        self.phases = self.data["phases"]

    def is_doable(self):
        if self.data["done"] == False:
            return True
        return False

    def get_enemy(self):
        if self.data["type"] == "fight":
            self.enemy_id = self.data["enemyId"]
            return True
        return False
