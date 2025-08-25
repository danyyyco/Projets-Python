import json
from colorama import init, Fore, Back, Style

init(autoreset=True)

# Nom du fichier de sauvegarde
SAVE_FILE = "contacts.json"

def load_contacts():
    """Charge les contacts depuis un fichier JSON"""
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(repertoire):
    """Sauvegarde les contacts dans un fichier JSON"""
    with open(SAVE_FILE, "w") as f:
        json.dump(repertoire, f, indent=4)

def display_menu():
    print(f"{Fore.CYAN}\n--- PHONE BOOK ---")
    print("1- Add a contact")
    print("2- Search a contact")
    print("3- Display Contacts")
    print("4- Delete a contact")
    print("5- Exit")

def add_contact(repertoire):
    name = input("\n Enter the name: ")
    number = input("\n Enter the number: ")
    repertoire[name] = number
    save_contacts(repertoire)  # sauvegarde après ajout
    print(f"\n{Fore.GREEN} Contact {name} successfully added with the number {Fore.MAGENTA}{number}")

def search_contact(repertoire):
    name = input("\n Enter the name to search: ")
    if name in repertoire:
        print(f"\n{Fore.GREEN} Contact found: {Fore.MAGENTA}{name} - {repertoire[name]}")
    else:
        print(f"\n{Fore.RED} No contact found with the name {Fore.MAGENTA}{name}")

def display_contacts(repertoire):
    if repertoire:
        print("\n--- CONTACTS LIST ---")
        for name, number in repertoire.items():
            print(f"{Fore.MAGENTA}{name}: {number}")
    else:
        print(f"\n{Fore.RED} No contact found in the phone book")

def delete_contact(repertoire):
    name = input("\n Enter the name to delete: ")
    if name in repertoire:
        del repertoire[name]
        save_contacts(repertoire)  # sauvegarde après suppression
        print(f"\n{Fore.GREEN} Contact {name} deleted successfully")
    else:
        print(f"\n{Fore.RED} No contact found with the name {Fore.MAGENTA}{name}")

# Charger les contacts existants au démarrage
repertoire = load_contacts()

while True:
    display_menu()
    try:
        user_choice = int(input(f"\n {Fore.BLUE} Enter your choice: "))
    except ValueError:
        print(f"\n{Fore.RED} Invalid input! Please enter a number.")
        continue

    if user_choice == 1:
        add_contact(repertoire)
    elif user_choice == 2:
        search_contact(repertoire)
    elif user_choice == 3:
        display_contacts(repertoire)
    elif user_choice == 4:
        delete_contact(repertoire)
    elif user_choice == 5:
        print(f"\n{Fore.MAGENTA} Good bye!")
        break
    else:
        print(f"\n{Fore.RED} Invalid choice! Retry")
