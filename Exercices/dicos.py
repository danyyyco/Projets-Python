voiture = {
    "marque": "Toyota",
    "couleur": "Bordeau",
    "immatriculation": "100SD45"
}

#Affichage du dico complet
print(voiture)

#Affichage de la marque
print(voiture["marque"])
print(voiture.get("marque"))

#Modif de la marque
voiture["marque"] = "Lamborghini"
print(voiture["marque"])

#Ajout d'un autre attribut
voiture["proprio"] = "Mike"
print(voiture)

del voiture["proprio"]
print(voiture)

voiture.pop("marque")
print(voiture)

for cle, val in voiture.items():
    # print(cle, val)
    print(f"{cle}:{val}")
    

contacts = {
    "Wendy": 100,
    "Max": 200
}

print(contacts)

contacts["Mel"] = 300

print(contacts)