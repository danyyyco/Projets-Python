# mini programme de gestion des contacts
import json
import os

FILE = "contactt.json"  # Définir le nom de mon fichier

# Charger les contacts depuis JSON
def charger_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Sauvegarder les contacts dans le fichier JSON
def sauvegarder_contacts(contacts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

# Ajouter un contact
def ajouter_contact(contacts):
    try:
        nom = input("Entrer le nom du contact : ")
        numero = input("Entrer le numéro du téléphone : ")
        email = input("Entrer l'email : ")
        adresse = input("Entrer l'adresse : ")

        contacts[nom] = {
            "Numero": numero,
            "Email": email,
            "Adresse": adresse
        }
        sauvegarder_contacts(contacts)
        print(f"Le contact {nom} ajouté avec succès ✅!")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Modifier un contact
def modifier_contact(contacts):
    nom = input("Entrer le nom du contact à modifier : ")
    if nom in contacts:
        print("Laisser vide si vous ne voulez pas changer un champ")
        numero = input(f"Entrer le nouveau numéro ({contacts[nom]['Numero']}) : ") or contacts[nom]["Numero"]
        email = input(f"Entrer le nouvel email ({contacts[nom]['Email']}) : ") or contacts[nom]["Email"]
        adresse = input(f"Entrer la nouvelle adresse ({contacts[nom]['Adresse']}) : ") or contacts[nom]["Adresse"]

        contacts[nom] = {
            "Numero": numero,
            "Email": email,
            "Adresse": adresse
        }
        sauvegarder_contacts(contacts)
        print(f"Le contact {nom} modifié avec succès 👍!")
    else:
        print(f"❌ Le contact n'existe pas.")

# Supprimer un contact
def supprimer_contact(contacts):
    nom = input("Entrer le nom à supprimer : ")
    if nom in contacts:
        del contacts[nom]
        sauvegarder_contacts(contacts)
        print(f"Le contact {nom} supprimé avec succès 🗑️!")
    else:
        print(f"❌ Le contact n'existe pas.")

# Rechercher un contact par nom
def rechercher_par_nom(contacts):
    nom = input("Entrer le nom à rechercher : ")
    if nom in contacts:
        infos = contacts[nom]
        print(f"\n📞 {nom} ")
        print(f"- Numero : {infos['Numero']}")
        print(f"- Email : {infos['Email']}")
        print(f"- Adresse : {infos['Adresse']}")
    else:
        print(f"❌ Le contact introuvable!")

# Rechercher un contact par numéro
def rechercher_par_numero(contacts):
    numero = input("Entrer le numéro à rechercher : ")
    trouve = False
    for nom, infos in contacts.items():
        if infos["Numero"] == numero:
            print(f"\n📞 {nom} ")
            print(f"- Numero : {infos['Numero']}")
            print(f"- Email : {infos['Email']}")
            print(f"- Adresse : {infos['Adresse']}")
            trouve = True
    if not trouve:
        print("❌ Aucun contact trouvé avec ce numéro.")

# Rechercher un contact par email
def rechercher_par_email(contacts):
    email = input("Entrer l'email à rechercher : ")
    trouve = False
    for nom, infos in contacts.items():
        if infos["Email"].lower() == email.lower():
            print(f"\n📞 {nom} ")
            print(f"- Numero : {infos['Numero']}")
            print(f"- Email : {infos['Email']}")
            print(f"- Adresse : {infos['Adresse']}")
            trouve = True
    if not trouve:
        print("❌ Aucun contact trouvé avec cet email.")

# Menu de recherche avancée
def menu_recherche(contacts):
    while True:
        print("\n--- Recherche avancée ---")
        print("1. Recherche par nom")
        print("2. Recherche par numéro")
        print("3. Recherche par email")
        print("4. Retour au menu principal")

        choix = input("Choisissez votre option : ")
        if choix == "1":
            rechercher_par_nom(contacts)
        elif choix == "2":
            rechercher_par_numero(contacts)
        elif choix == "3":
            rechercher_par_email(contacts)
        elif choix == "4":
            break
        else:
            print("❌ Choix invalide, réessayez!")

# Afficher tous les contacts
def afficher_contacts(contacts):
    if contacts:
        print(f"\n📒 Liste des contacts : ")
        for nom, infos in contacts.items():
            print(f"\n👩 {nom} ")
            print(f"- Numero : {infos['Numero']}")
            print(f"- Email : {infos['Email']}")
            print(f"- Adresse : {infos['Adresse']}")
    else:
        print(f"❌ Aucun contact enregistré !")

# Menu principal
def menu():
    contacts = charger_contacts()
    while True:
        print("\n--- Répertoire téléphonique ---")
        print("1. Ajouter un contact")
        print("2. Modifier un contact")
        print("3. Supprimer un contact")
        print("4. Rechercher un contact")
        print("5. Afficher tous les contacts")
        print("6. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_contact(contacts)
        elif choix == "2":
            modifier_contact(contacts)
        elif choix == "3":
            supprimer_contact(contacts)
        elif choix == "4":
            menu_recherche(contacts)
        elif choix == "5":
            afficher_contacts(contacts)
        elif choix == "6":
            print("Merci d'avoir utilisé le répertoire. Au revoir 🖐️!")
            break
        else:
            print("❌ Choix invalide, réessayez!")

# Lancer le programme
menu()
