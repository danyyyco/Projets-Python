# Importation de colorama
from colorama import Fore, Style

import time, json, os

SAVE_FILE = "contacts.json"


def charger_contacts():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def sauvegarder_contacts():
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(Fore.RED + f"❌ Erreur de sauvegarde: {e}")


contacts = charger_contacts()


def menu():
    text = "\n=== MENU REPERTOIRE ==="
    print(Fore.CYAN + Style.BRIGHT + text.center(50, " ") + Style.RESET_ALL)
    print(Fore.YELLOW + "1 -" + Style.RESET_ALL + " Afficher le répertoire")
    print(Fore.YELLOW + "2 -" + Style.RESET_ALL + " Ajouter un contact")
    print(Fore.YELLOW + "3 -" + Style.RESET_ALL + " Rechercher un contact")
    print(Fore.YELLOW + "4 -" + Style.RESET_ALL + " Modifier un contact")
    print(Fore.YELLOW + "5 -" + Style.RESET_ALL + " Supprimer un contact")
    print(Fore.YELLOW + "6 -" + Style.RESET_ALL + " Quitter")

def afficher_contacts():
    if not contacts:
        print(Fore.RED + "\n❌ Aucun contact dans le répertoire.")
    else:
        print(Fore.GREEN + Style.BRIGHT + "\n=== MON REPERTOIRE === ")
        for nom, numero in contacts.items():
            print(Fore.WHITE + f"{nom} : {numero}")

def ajouter_contact():
    try:
        nom = input("Entrez le nom: ").strip().lower()
        numero = input("Entrez le numéro: ").strip()

        if nom in contacts:
            print(Fore.RED + f"\n❌ Le contact '{nom}' existe déjà avec le numéro {contacts[nom]}")
        else:
            contacts[nom] = numero
            sauvegarder_contacts()
            print(Fore.GREEN + f"\n✅ Le contact '{nom}' : {numero} a bien été ajouté.")
    except Exception as e:
        print(Fore.RED + f"Erreur lors de l'ajout: {e}")

def rechercher_contact():
    nom = input("Entrez le nom du contact à rechercher: ").strip().lower()
    if not contacts:
        print(Fore.RED + "\n⚠ Impossible de rechercher dans un répertoire vide.")
    elif nom in contacts:
        print(Fore.GREEN + f"\n🔍 Contact trouvé: {nom} : {contacts[nom]}")
    else:
        print(Fore.RED + f"\n❌ Aucun contact nommé '{nom}' trouvé.")

def modifier_contact():
    nom_actuel = input("Entrez le nom actuel du contact à modifier: ").strip().lower()
    if nom_actuel in contacts:
        numero_actuel = contacts[nom_actuel]
        print(Fore.GREEN + f"Contact trouvé: {nom_actuel} : {numero_actuel}")

        choix = input("Voulez-vous modifier (1) le nom, (2) le numéro, ou (3) les deux ? ").strip()
        
        if choix == '1':
            nouveau_nom = input("Entrez le nouveau nom: ").strip().lower()
            contacts[nouveau_nom] = contacts.pop(nom_actuel)
            print(Fore.GREEN + f"✅ Le contact a été modifié: {nouveau_nom} : {numero_actuel}")
        
        elif choix == '2':
            nouveau_numero = input("Entrez le nouveau numéro: ").strip()
            contacts[nom_actuel] = nouveau_numero
            print(Fore.GREEN + f"✅ Le numéro de '{nom_actuel}' a été modifié: {nouveau_numero}")
        
        elif choix == '3':
            nouveau_nom = input("Entrez le nouveau nom: ").strip().lower()
            nouveau_numero = input("Entrez le nouveau numéro: ").strip()
            contacts[nouveau_nom] = nouveau_numero
            del contacts[nom_actuel]
            print(Fore.GREEN + f"✅ Le contact a été modifié: {nouveau_nom} : {nouveau_numero}")
        
        else:
            print(Fore.RED + "❌ Choix invalide. Aucune modification effectuée.")

        sauvegarder_contacts()
    else:
        print(Fore.RED + f"\n❌ Le contact '{nom_actuel}' n'existe pas.")

def supprimer_contact():
    nom_contact_a_suppr = input("Entrez le nom du contact à supprimer: ").strip().lower()
    if nom_contact_a_suppr in contacts:
        confirmation = input(Fore.YELLOW + f"⚠ Voulez-vous vraiment supprimer '{nom_contact_a_suppr}' ? (O/N): ").strip().lower()
        if confirmation == "o":
            del contacts[nom_contact_a_suppr]
            sauvegarder_contacts()
            print(Fore.GREEN + "✅ Contact supprimé avec succès.")
        else:
            print(Fore.CYAN + "❎ Suppression annulée.")
    else:
        print(Fore.RED + "❌ Contact introuvable.")



while True:
    time.sleep(2)
    menu()
    try:
        choix = int(input(Fore.CYAN + "\nEntrez votre choix: " + Style.RESET_ALL))
        
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
            print(Fore.MAGENTA + Style.BRIGHT + "\n👋 Au revoir !" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\n❌ Choix invalide. Veuillez entrer un nombre entre 1 et 6.")
    except ValueError:
        print(Fore.RED + "⚠ Erreur: Veuillez entrer un nombre valide (1 à 6).")
    except Exception as e:
        print(Fore.RED + f"⚠ Une erreur est survenue: {e}")
