import json

some_data = { "jmeno" : "lala",
              "characterclass" : "warrior"
         }

# ulozi data do souboru ( 'w' - write )
with open("json_test.json", 'w') as file:
    json.dump(some_data, file)

# nacte data ze souboru ( 'r' - read )
with open("json_test.json", 'r') as file:
    nacteny_data = json.load(file)

print(nacteny_data["jmeno"])
print()

some_data["bla"] = "Fn"

print(some_data)

with open("json_test.json", 'w') as file:
    json.dump(some_data, file)