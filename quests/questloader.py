import os
import json

class Questloader():
    def __init__(self, questnr):
        self.path_to_file = os.path.normpath("quests/data/%s.json" %questnr)
        try:
            with open(self.path_to_file, 'r') as file:
                self.json_data = json.load(file)            
        except IOError:
            print("Error reading file")

    def save_and_close_json(self, new_data):
        try:
            with open(self.json_data, 'w') as file:
                json.dump(new_data, file)
        except IOError:
            print("Error saving to file")