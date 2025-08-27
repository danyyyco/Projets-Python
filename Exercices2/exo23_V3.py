# --- IMPORTS ---
from colorama import init, Fore, Style
import time
import json
import os

# Initialisation Colorama
init(autoreset=True)

# --- CONSTANTES ---
FICHIER_CONTACTS = "contacts.json"

# --- DONNÉES ---
contacts = {}

# --- FONCTIONS DE SAUVEGARDE ---
def charger_contacts():
    global contacts
    if os.path.exists(FICHIER_CONTACTS):
        try:
            with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
                contacts = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            contacts = {}
    else:
        contacts = {}

def sauvegarder_contacts():
    with open(FICHIER_CONTACTS, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

# --- FONCTIONS PRINCIPALES ---

def menu():
    print(Fore.CYAN + Style.BRIGHT + "\n=== MENU REPERTOIRE ===")
    print(Fore.YELLOW + "1- Afficher le répertoire")
    print("2- Ajouter un contact")
    print("3- Rechercher un contact")
    print("4- Modifier un contact")
    print("5- Supprimer un contact")
    print("6- Quitter")

def afficher_contacts():
    if not contacts:
        print(Fore.RED + "\n⚠️ Aucun contact dans le répertoire.")
    else:
        print(Fore.GREEN + Style.BRIGHT + "\n=== MON REPERTOIRE === ")
        for nom_cle, infos in contacts.items():
            nom, numero = infos
            print(Fore.WHITE + f"📞 {nom}: {numero}")

def ajouter_contact():
    try:
        nom = input(Fore.CYAN + "Entrez le nom: ").strip()
        numero = input(Fore.CYAN + "Entrez le numéro: ").strip()

        if not numero.isdigit():
            print(Fore.RED + "❌ Erreur : Le numéro doit être composé uniquement de chiffres.")
            return

        nom_cle = nom.lower()

        if nom_cle in contacts:
            print(Fore.YELLOW + f"⚠️ Le contact {nom} existe déjà avec le numéro {contacts[nom_cle][1]}.")
        else:
            contacts[nom_cle] = (nom, numero)
            sauvegarder_contacts()
            print(Fore.GREEN + f"✅ Le contact {nom}: {numero} a bien été ajouté.")
    except Exception as e:
        print(Fore.RED + f"❌ Erreur lors de l'ajout : {e}")

def rechercher_contact():
    nom = input(Fore.CYAN + "Entrez le nom du contact à rechercher: ").strip()
    nom_cle = nom.lower()

    if not contacts:
        print(Fore.RED + "⚠️ Impossible de rechercher dans un répertoire vide.")
    elif nom_cle in contacts:
        vrai_nom, numero = contacts[nom_cle]
        print(Fore.GREEN + f"✅ Contact trouvé : {vrai_nom}: {numero}")
    else:
        print(Fore.RED + f"❌ Aucun contact nommé {nom} trouvé.")

def modifier_contact():
    nom_actuel = input(Fore.CYAN + "Entrez le nom actuel du contact à modifier: ").strip()
    nom_cle = nom_actuel.lower()

    if nom_cle in contacts:
        vrai_nom, numero_actuel = contacts[nom_cle]
        print(Fore.GREEN + f"✅ Contact trouvé : {vrai_nom}: {numero_actuel}")

        choix = input(Fore.YELLOW + "Voulez-vous modifier (1) le nom, (2) le numéro, (3) les deux ? ").strip()

        if choix == '1':
            nouveau_nom = input("Entrez le nouveau nom: ").strip()
            contacts.pop(nom_cle)
            contacts[nouveau_nom.lower()] = (nouveau_nom, numero_actuel)
            sauvegarder_contacts()
            print(Fore.GREEN + f"✅ Le nom a été modifié : {nouveau_nom}: {numero_actuel}")

        elif choix == '2':
            nouveau_numero = input("Entrez le nouveau numéro: ").strip()
            if not nouveau_numero.isdigit():
                print(Fore.RED + "❌ Erreur : Le numéro doit être composé uniquement de chiffres.")
                return
            contacts[nom_cle] = (vrai_nom, nouveau_numero)
            sauvegarder_contacts()
            print(Fore.GREEN + f"✅ Le numéro a été modifié : {vrai_nom}: {nouveau_numero}")

        elif choix == '3':
            nouveau_nom = input("Entrez le nouveau nom: ").strip()
            nouveau_numero = input("Entrez le nouveau numéro: ").strip()
            if not nouveau_numero.isdigit():
                print(Fore.RED + "❌ Erreur : Le numéro doit être composé uniquement de chiffres.")
                return
            contacts.pop(nom_cle)
            contacts[nouveau_nom.lower()] = (nouveau_nom, nouveau_numero)
            sauvegarder_contacts()
            print(Fore.GREEN + f"✅ Contact modifié : {nouveau_nom}: {nouveau_numero}")

        else:
            print(Fore.RED + "❌ Choix invalide. Aucune modification effectuée.")
    else:
        print(Fore.RED + f"❌ Le contact {nom_actuel} n'est pas dans le répertoire.")

def supprimer_contact():
    nom = input(Fore.CYAN + "Entrez le nom du contact à supprimer: ").strip()
    nom_cle = nom.lower()
    if nom_cle in contacts:
        contacts.pop(nom_cle)
        sauvegarder_contacts()
        print(Fore.GREEN + "✅ Contact supprimé avec succès.")
    else:
        print(Fore.RED + "❌ Contact introuvable.")

# --- PROGRAMME PRINCIPAL ---
charger_contacts()

while True:
    time.sleep(0.5)
    menu()
    try:
        choix = input(Fore.CYAN + "\n👉 Entrez votre choix: ").strip()
        if not choix.isdigit():
            print(Fore.RED + "❌ Erreur : veuillez entrer un nombre.")
            continue
        choix = int(choix)

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
            print(Fore.MAGENTA + Style.BRIGHT + "👋 Au revoir !")
            break
        else:
            print(Fore.RED + "❌ Choix invalide, veuillez réessayer.")

    except Exception as e:
        print(Fore.RED + f"❌ Erreur inattendue : {e}")
