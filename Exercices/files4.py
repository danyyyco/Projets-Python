chemin = r"C:\Users\dimit\Documents\source.txt"
mot_utilisateur = input("Entre un mot: ")

with open(chemin, "r") as file:
    contenu = file.read()
    mots = contenu.split()
    for mot in mots:
        if mot.lower() == mot_utilisateur.lower():
            print(f"Le mot {mot_utilisateur} a été trouvé dans le fichier")
            break
    else:
        print(f"Le mot {mot_utilisateur} n'a pas été trouvé dans le fichier")