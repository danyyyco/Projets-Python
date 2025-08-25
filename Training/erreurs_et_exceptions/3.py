try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Erreur: Vous avez entré un texte au lieu d'un nombre")