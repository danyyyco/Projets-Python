import random

score = 0
choix = "y"

while choix.lower() == "y":
    r = random.randrange(1, 101)
    nb_essais = 0

    while nb_essais <= 7:
        nb_utilisateur = int(input("Devinez le nombre (entre 1 et 100) : "))

        if nb_utilisateur == r:
            print(f"Félicitations ! Vous avez deviné le nombre {r} en {nb_essais} essais !")
            score += 1
            break
        elif nb_utilisateur > r:
            print("C'est moins !")
        elif nb_utilisateur < r:
            print("C'est plus !")

        nb_essais += 1

    if nb_essais > 7:
        print(f"\033[31m Désolé, vous avez perdu \033[0m!  Le nombre était : {r}")

    print("Score final :", score)

    choix = input("Voulez-vous jouer à nouveau ? (y/n) : ")
    if choix.lower() == "n":
        print("Merci d'avoir joué !")
