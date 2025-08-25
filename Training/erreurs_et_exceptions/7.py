nom_fichier = input("Veuillez entrer le nom du fichier à lire : ")

try:
    # Tentative d'ouverture du fichier en mode lecture
    fichier = open(nom_fichier, 'r')
    contenu = fichier.read()
    print("Contenu du fichier :")
    print(contenu)

except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")

finally:
    # Assurez-vous que le fichier est fermé
    try:
        fichier.close()
    except NameError:
        # Si 'fichier' n'a jamais été défini (dans le cas d'une exception)
        pass