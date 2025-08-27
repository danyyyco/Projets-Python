#importation de colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

import time

#initialisation de mon repertoire
contacts = {}

# --- FONCTIONS ---

#menu
def menu():
    print(Fore.CYAN + "\n=== MENU REPERTOIRE ===")
    print("\n1- 📖 Afficher le répertoire")
    print("2- ➕ Ajouter un contact")
    print("3- 🔍 Rechercher un contact")
    print("4- ✏️ Modifier un contact")
    print("5- ❌ Supprimer un contact")
    print("6- 🚪 Quitter")

#afficher_contacts
def afficher_contacts():
    #on verifie si le repertoire est vide
    if not contacts:
        print(Fore.YELLOW + "\nAucun contact 😢")
    #sinon
    else:
        print(Fore.GREEN + "\n=== MON REPERTOIRE === ")
        for nom, numero in contacts.items():
            print(f"\n{nom}: {numero}")

#ajouter un contact
def ajouter_contact():
    nom_original = input("Entrez le nom: ")
    nom = nom_original.lower()
    numero = int(input("Entrez le numéro: ")) 
    #On verifie si le nom est déjà dans le repertoire
    if nom in contacts:
        print(Fore.YELLOW + f"\nLe contact {nom} est déjà dans le répertoire avec le numéro {contacts[nom]} 📞")
    #sinon
    else:
        contacts[nom] = numero
        print(Fore.GREEN + f"\nLe contact {nom}: {numero} a bien été ajouté au répertoire ✅")

#recherche de contact
def rechercher_contact():
    nom_original = input("Entrez le nom du contact à rechercher: ")
    nom = nom_original.lower()
    if not contacts:
        print(Fore.YELLOW + "\nAucun contact! On ne peut effectuer une recherche dans un répertoire vide. 😔")
    elif nom in contacts:
        print(Fore.GREEN + f"\nContact trouvé: {nom}: {contacts[nom]} ✅")
    else:
        print(Fore.RED + f"\nAucun(e) {nom} trouvé ❌")
        
def modifier_contact():
    nom_original = input("Entrez le nom actuel du contact à modifier: ")
    nom_actuel = nom_original.lower()

    if nom_actuel in contacts:
        # Obtenir le numéro actuel
        numero_actuel = contacts[nom_actuel]
        print(Fore.GREEN + f"Contact trouvé: {nom_actuel}: {numero_actuel}")
        
        # Demander ce que l'utilisateur souhaite modifier
        choix = input("Voulez-vous modifier (1) le nom, (2) le numéro, ou (3) les deux? Entrez 1, 2 ou 3: ")
        
        if choix == '1':
            nouveau_nom = input("Entrez le nouveau nom: ")
            contacts[nouveau_nom] = contacts.pop(nom_actuel)  # Modifier uniquement le nom
            print(Fore.GREEN + f"Le contact a été modifié: {nouveau_nom}: {numero_actuel} ✅")
        
        elif choix == '2':
            nouveau_numero = input("Entrez le nouveau numéro: ")
            contacts[nom_actuel] = nouveau_numero  # Modifier uniquement le numéro
            print(Fore.GREEN + f"Le numéro a été modifié pour le contact {nom_actuel}: {nouveau_numero} ✅")
        
        elif choix == '3':
            nouveau_nom = input("Entrez le nouveau nom: ")
            nouveau_numero = input("Entrez le nouveau numéro: ")
            contacts[nouveau_nom] = nouveau_numero  # Modifier les deux
            del contacts[nom_actuel]  # Supprimer l'ancien contact
            print(Fore.GREEN + f"Le contact a été modifié: {nouveau_nom}: {nouveau_numero} ✅")
        
        else:
            print(Fore.RED + "Choix invalide. Aucune modification effectuée.")
    
    else:
        print(Fore.RED + f"\nLe contact {nom_actuel} n'est pas dans le répertoire. ❌")

            
def supprimer_contact():
    nom_original = input("Entrez le nom du contact à supprimer: ")
    nom_contact_a_suppr = nom_original.lower()
    if nom_contact_a_suppr in contacts:
        del contacts[nom_contact_a_suppr]
        print(Fore.GREEN + "\nContact supprimé avec succès ✅")
    else:
        print(Fore.RED + "\nContact introuvable ❌")
        
#Boucle Principale            
while True:
    time.sleep(1)
    menu()
    choix = int(input("\nEntrez votre choix: "))
    if choix == 1:
        afficher_contacts()
    elif choix == 2:
        ajouter_contact()
    elif choix == 3:
        rechercher_contact()
    elif choix == 4:
        modifier_contact()
    elif choix == 5:
        supprimer_contact()
    elif choix == 6:
        print(Fore.BLUE + "Au revoir! 👋")
        break
    else:
        print(Fore.RED + "\nChoix invalide ❌")
