def diviser(a, b):
    """Divise a par b et lève une ValueError si b est zéro."""
    if b == 0:
        raise ValueError("Erreur : Division par zéro n'est pas autorisée.")
    return a / b


def main():
    try:
        # Demande à l'utilisateur d'entrer les valeurs pour a et b
        a = float(input("Veuillez entrer le numérateur (a) : "))
        b = float(input("Veuillez entrer le dénominateur (b) : "))

        # Appel de la fonction de division
        resultat = diviser(a, b)
        print(f"Le résultat de {a} / {b} est : {resultat}")

    except ValueError as e:
        # Gestion de l'exception ValueError
        print(e)


# Exécution du programme principal
if __name__ == "__main__":
    main()
