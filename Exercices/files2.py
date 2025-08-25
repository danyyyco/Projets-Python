import json

chemin = "/Users/thibh/fichier.json"

with open(chemin, "w") as f:
    json. dump("Bonjour", f)


with open(chemin, "w") as f:
    json.dump(list(range(10)), f, indent=4)

with open(chemin, "r") as f:
    liste = json. load(f)
    print(type(liste))