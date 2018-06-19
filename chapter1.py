import json
from deffschapter1 import dialog1

with open("dchapter1check.json", 'r') as file:
    dchapter1check = json.load(file)
with open("dchapter1.json", 'r') as file:
    dchapter1 = json.load(file)

dialog1()
