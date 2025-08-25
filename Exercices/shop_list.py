
from colorama import init, Fore, Back, Style
init(autoreset = True)

shop_list = list()

while True:
    print("\n === GESTION DES COURSES ===")
    print(Fore.BLUE + "1- Afficher la liste de courses")
    print(Fore.BLUE + "2- Ajouter un article")
    print(Fore.BLUE + "3- Supprimer un article")
    print(Fore.BLUE + "4- Vider la liste")
    print(Fore.BLUE + "5- Quitter")

    choix = int(input(Fore.YELLOW + "\nVotre choix: "))
    if choix == 1:
            if not shop_list:
                print(Fore.RED + "\nAucun article dispo")
            else:
                for index, article in enumerate(shop_list):
                    print(Fore.BLUE + f"{index + 1}.{article}")

    elif choix == 2:
        nouvel_article = input("\nEntrer le nouvel article: ")
        if nouvel_article in shop_list:
            print(Fore.RED + f"L'article {nouvel_article} existe déjà!")
        else:
            shop_list.append(nouvel_article)
            print(Fore.GREEN + f"\nArticle {nouvel_article} ajouté avec succès!")

    elif choix == 3:
        article_a_supprimer = input("\nEntrer le nom de l'article à supprimer: ")
        if article_a_supprimer in shop_list:
            shop_list.remove(article_a_supprimer)
            print(Fore.GREEN + f"\nArticle {article_a_supprimer} supprimé avec succès!")
        else:
            print(Fore.RED + f"\nL'artcile {article_a_supprimer} n'existe pas!")

    elif choix == 4:
        if not shop_list:
            print(Fore.RED + "\nOn ne peut supprimer une liste vide")
        else:
            shop_list.clear()
            print(Fore.GREEN + "\nListe vidée avec succès!")

    elif choix == 5:
        print(Fore.MAGENTA + "Au revoir!")
        break

    else:
        print(Fore.RED + "\nErreur! Choix invalide")