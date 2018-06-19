import json


with open("dchapter1check.json", 'r') as file:
    dchapter1check = json.load(file)
with open("dchapter1.json", 'r') as file:
    dchapter1 = json.load(file)


if dchapter1check["Prvni kecy"] == 0:
    print(dchapter1["Dialog1"])
    dchapter1check["Prvni kecy"] = 1
    with open("dchapter1check.json", 'w') as file:
        json.dump(dchapter1check, file)