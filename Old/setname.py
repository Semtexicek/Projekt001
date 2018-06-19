import json

####Pokus o definici pro nastaveni jmena
def setname():
    with open("bestiar.json", 'r') as file:
        setname = json.load(file)

    x = input("Write nick:")
    setname["nick"] = x
    
    with open("bestiar.json", 'w') as file:
        json.dump(setname, file)
