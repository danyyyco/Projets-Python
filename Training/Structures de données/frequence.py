def compter_frequence(chaine):
    # Créer un dictionnaire pour stocker la fréquence des caractères
    frequence = {}

    # Parcourir chaque caractère dans la chaîne
    for caractere in chaine:
        # Si le caractère est déjà dans le dictionnaire, on incrémente sa fréquence
        if caractere in frequence:
            frequence[caractere] += 1
        else:
            # Sinon, on l'ajoute avec une fréquence de 1
            frequence[caractere] = 1

    return frequence


# Exemple d'utilisation
chaine = input("Entrez une chaîne de caractères : ")
resultat = compter_frequence(chaine)

# Afficher le dictionnaire résultant
print("Fréquence des caractères :", resultat)
