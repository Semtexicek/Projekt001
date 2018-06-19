import json

####Tady bych zhromazdoval definice, co napiseme, protoze uz vidim, ze nechceme mit soubor pro kazdou###


### Nastaveni nicku ###
def setname():
    with open("bestiar.json", 'r') as file:
        setname = json.load(file)

    x = input("Write nick:")
    setname["nick"] = x
    
    with open("bestiar.json", 'w') as file:
        json.dump(setname, file)

### Restart bestiare ###

bestiar = {
    "nick" : "xy",
    "class" : "xy",
    "sila" : "xy",
    "dex" : "xy",
    "int" : "xy"
}
def restart():
    with open("bestiar.json", 'w') as file:
        json.dump(bestiar, file)