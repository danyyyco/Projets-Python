import random, os, json

from colorama import init, Fore, Back, Style
init(autoreset=True)

# === FICHIER DE SAUVEGARDE ===
SAVE_FILE = "joueurs.json"

# Charger les données des joueurs
def charger_donnees():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {}

# Sauvegarder les données des joueurs
def sauvegarder_donnees(donnees):
    with open(SAVE_FILE, "w") as f:
        json.dump(donnees, f, indent=4)

# Charger les stats existantes
joueurs = charger_donnees()

# Message de bienvenue
print(Back.BLUE + Fore.LIGHTWHITE_EX + Style.BRIGHT + "\n === BIENVENUE AU GUESS GAME!  === 🎉" + Style.RESET_ALL)

# Prénom utilisateur
prenom_utilisateur = input(Fore.CYAN + Style.BRIGHT + "\nQuel est ton prénom, jeune pandawan ? 🎮 : " + Style.RESET_ALL)

# Si le joueur existe déjà on charge ses stats, sinon on initialise
if prenom_utilisateur in joueurs:
    score = joueurs[prenom_utilisateur]["score"]
    nb_jeux_joues = joueurs[prenom_utilisateur]["nb_jeux_joues"]
    nb_victoires = joueurs[prenom_utilisateur]["nb_victoires"]
    print(Fore.GREEN + f"\n🔥 Re-bienvenue {prenom_utilisateur} ! Tes stats sont sauvegardées, les voici :")
else:
    score = 0
    nb_jeux_joues = 0
    nb_victoires = 0
    joueurs[prenom_utilisateur] = {"score": 0, "nb_jeux_joues": 0, "nb_victoires": 0}
    print(Fore.MAGENTA + f"\n✨ Bienvenue {prenom_utilisateur}! C'est ta première partie, bonne chance ! 🚀")

# Fonction lancer_jeu
def lancer_jeu(nb_essais_max, plafond, mode_nom):
    global score, nb_jeux_joues, nb_victoires
    nb_essais = 1
    r = random.randint(1,plafond)
    gagne = False
    
    print(Back.CYAN + Fore.BLACK + f"\n 🎲 🌱 Mode {mode_nom} activé ! Devine un nombre entre 1 et {plafond} avec {nb_essais_max} essais maximum ! 💡" + Style.RESET_ALL)
    
    while nb_essais <= nb_essais_max:
            nb_utilisateur = int(input(Fore.YELLOW + f"\n👉 {prenom_utilisateur}, devine le nombre : " + Style.RESET_ALL))
            if nb_utilisateur == r:
                print(Fore.GREEN + f"\n🎉 Bravo {prenom_utilisateur} ! Tu as trouvé le nombre {r} en {nb_essais} essais ! 🏆")
                score += 1
                nb_victoires += 1
                gagne = True
                break
            elif nb_utilisateur < r:
                print(Fore.RED + "\n📈 C'est plus! Essaie avec un nombre plus grand ⬆️")
            elif nb_utilisateur > r:
                print(Fore.BLUE + "\n📉 C'est moins ! Essaie un plus petit nombre ⬇️")
            else:
                print (Fore.RED + "\n⚠️ Ce n'est pas un nombre valide ! 🔢")

            nb_essais += 1

    if not gagne:
        print(Fore.RED + f" \n 💀Oups! {prenom_utilisateur}... tu as épuisé tes essais ! Le nombre était {r} 🎯")
    
    nb_jeux_joues += 1
    taux_reussite = (nb_victoires / nb_jeux_joues) * 100
    
    print(Style.BRIGHT + Fore.CYAN + f"\n📊 Statistiques de {prenom_utilisateur} :")
    print(Fore.YELLOW + f"⭐ Score : {score}")
    print(Fore.YELLOW + f"🎮 Parties jouées : {nb_jeux_joues}")
    print(Fore.YELLOW + f"🏆 Victoires : {nb_victoires}")
    print(Fore.YELLOW + f"📈 Taux de reussite : {taux_reussite:.2f}%")
    
    # Sauvegarde après chaque partie
    joueurs[prenom_utilisateur] = {
        "score": score,
        "nb_jeux_joues": nb_jeux_joues,
        "nb_victoires": nb_victoires
    }
    sauvegarder_donnees(joueurs)
    
    
    
#Boucle Principale
choix_continuer = "o"
while choix_continuer.lower() == 'o':
    print(Back.CYAN + Fore.LIGHTWHITE_EX + "\n === Choisis ton niveau de difficulté === 🏆" + Style.RESET_ALL)
    print(Fore.YELLOW + "\n 1️⃣ Facile (1-50, 10 essais) 🌱")
    print(Fore.YELLOW + "️2️⃣ Moyen (1-100, 7 essais) 🌱")
    print(Fore.YELLOW + "️3️⃣ Difficile (1-200, 10 essais) 🌱")

    choix_difficulte = int(input(("\n Entre le numéro de ton choix (1-3) 🎯 :")))

    if choix_difficulte == 1:
        lancer_jeu(10,50, "Facile")

    elif choix_difficulte == 2:
        lancer_jeu(7,100, "Moyen")
        
    elif choix_difficulte == 3:
        lancer_jeu(5,200, "Difficile")
     
    else:
        print(Fore.RED + "❌ Choix invalide, essaie encore !")

    choix_continuer = input(Fore.MAGENTA + "\n Veux-tu continuer?(o:oui/n:non)" + Style.RESET_ALL)

#Message d' Aurevoir
if choix_continuer.lower() == "n":
    print(Fore.GREEN + f"👋 Merci d'avoir joué {prenom_utilisateur} ! Reviens vite pour plus de défis 🤩 !")