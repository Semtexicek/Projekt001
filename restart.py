import json

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