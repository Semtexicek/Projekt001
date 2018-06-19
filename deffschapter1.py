import json

with open("dchapter1check.json", 'r') as file:
    dchapter1check = json.load(file)
with open("dchapter1.json", 'r') as file:
    dchapter1 = json.load(file)

def dialog1():
    if dchapter1check["Prvni kecy"] == 0:
        print(dchapter1["Dialog1"] + "What's ur move?:" + '\n'"a) Projit se po jeskyni, porozhlednout se." + '\n'"b) Jit k mrizim a popovidat si se straznymi." + '\n'"c) Porozhlednout se po skupinkach, co jsou zac." + '\n'"d) Prohlednout si samotare.")
        x = input("")
    if x == "a":
        print("Projit se po jeskyni")
    elif x == "b":
        print("Jit k mrizim")
    elif x == "c":
        print("Porozhlednout se")


    dchapter1check["Prvni kecy"] = 1
    with open("dchapter1check.json", 'w') as file:
        json.dump(dchapter1check, file)

    