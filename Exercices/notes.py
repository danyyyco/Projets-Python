import time

NOTE_FILE = "notes.txt"

def show_menu():
    print("\n=== PRISE DE NOTES MENU ===")
    print("\n1- Voir mes notes")
    print("2- Ajouter une note")
    print("3- Modifier une note")
    print("4- Supprimer une note")
    print("5- Quitter")

    
# def voir_notes():
#     with open(NOTE_FILE, 'r') as f:
#         contenu = f.read()
#         if contenu:
#             print(contenu)
#         else:
#             print("\nRien à afficher")
            
def voir_notes():
    try:
        with open(NOTE_FILE, 'r') as f:
            contenu = f.read()
            if contenu:
                print("\n=== MES NOTES ===")
                print(contenu)
            else:
                print("\nRien à afficher")
    except FileNotFoundError:
        print(f"\nLe fichier {NOTE_FILE} auquel vous souhaitez accéder n'existe pas")
    except IOError:
        print(f"\nErreur lors de la lecture du fichier")
        

def ajouter_note():
    note = input("\nEntrez une note: ")
    print('\n')
    with open(NOTE_FILE, 'a') as f:
        f.write(note + "\n")
    print("\nNote ajouté avec succès")
    

# def supprimer_note():
#    voir_notes()
#    a_supp = input("Quelle note voulez-vous supprimer?")
   
        
def supprimer_notes():
    confirmation = input("\nÊtes-vous certain de vouloir supprimer toutes les notes ? (oui/non) ").strip().lower()
    if confirmation == "oui":
        with open(NOTE_FILE, "w") as f:
            f.write("")
        print("\nToutes les notes ont été supprimées.")
    elif confirmation == "non":
        print("\nSuppression annulée.")
    else:
        print("\nChoix invalide; Entrez soit 'oui' soit 'non'.")

while True:
    
    time.sleep(3)
    show_menu()
    
    try:
        choix = int(input("\nEntrez votre choix: "))
    except:
        print("\n Choix invalide; Entrez entre 1,2,3,4 ou 5")
    
    if choix == 1:
        voir_notes()
    elif choix == 2:
        ajouter_note()
    elif choix == 4:
        supprimer_notes()
    elif choix == 5:
        print("\nBye!\n")
        break
    else:
        print("\nEntrée invalide")