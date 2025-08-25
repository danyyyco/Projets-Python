nombre = input("Veuillez entrer un nombre à 4 chiffres : ")

if len(nombre) == 4 and nombre.isdigit():
    somme = sum(int(chiffre) for chiffre in nombre)
    print("La somme des chiffres est :", somme)
else:
    print("Veuillez entrer un nombre valide à 4 chiffres.")