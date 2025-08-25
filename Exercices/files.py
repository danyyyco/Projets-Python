import json

chemin = r"C:\Users\dimit\Documents\fichi.json"

"""with open(chemin, "r" ,encoding="utf-8") as f:
    content = f.read()
    print(content)"""

#with open(chemin, "w" ,encoding="utf-8") as f:
    #f.write("Yaya")

#with open(chemin, "a", encoding="utf-8") as f:
        #f.write("\nYaya")

#with open(chemin, "w+" ,encoding="utf-8") as f:
    #f.write("Yoyo")
    #f.seek(0)
    #content = f.read()
    #print(content)

#with open(chemin, "a+" ,encoding="utf-8") as f:
    #f.write("\nYaya")
    #f.seek(0)
    #content = f.read()
    #print(content)


#with open(chemin, "w") as f:
    #json.dump("Bonjour", f)

#with open(chemin, "w") as f:
    #json.dump(list(range(10)), f, indent=4)

with open(chemin, "r") as f:
    liste = json.load(f)
    print(liste) # affiche [0,1,2,3,4,5,6,7,8,9,11,10]
    print(type(liste))

liste.append(10) # On ajoute 11

with open(chemin, "w") as f:
    json.dump(liste, f, indent=4) # affiche [0,1,2,3,4,5,6,7,8,9,11,10]

with open(chemin, "r") as f:
    liste = json.load(f)
    print(liste) # affiche [0,1,2,3,4,5,6,7,8,9,11,10]
    print(type(liste))