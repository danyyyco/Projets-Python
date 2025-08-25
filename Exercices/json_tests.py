import json

chemin = r"C:\Users\dimit\Documents\test.json"

# with open(chemin, "w") as f:
    # json.dump("Hi!", f) #affiche Hi! dans le fichier .json
    # json.dump(list(range(10)), f) #Affiche [0,...,9]
    # json.dump(list(range(10)), f, indent=4)

# with open(chemin, "a") as f:
#      json.dump([10], f, indent=4)
    
with open(chemin, "r") as f:
    liste = json.load(f)
    # print(liste)
    
# print(liste)
liste.append(10)

with open(chemin, "w") as f:
    json.dump(liste, f, indent=4)