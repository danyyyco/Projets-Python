import random, os, json, time

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

# Prénom utilisateur (gestion insensible à la casse)
prenom_utilisateur_original = input(Fore.CYAN + Style.BRIGHT + "\nQuel est ton prénom, jeune pandawan ? 🎮 : " + Style.RESET_ALL).strip()
prenom_utilisateur = prenom_utilisateur_original.lower()  # normalisation

# Si le joueur existe déjà on charge ses stats, sinon on initialise
if prenom_utilisateur in joueurs:
    score = joueurs[prenom_utilisateur]["score"]
    nb_jeux_joues = joueurs[prenom_utilisateur]["nb_jeux_joues"]
    nb_victoires = joueurs[prenom_utilisateur]["nb_victoires"]
    print(Fore.GREEN + f"\n🔥 Re-bienvenue {prenom_utilisateur_original} ! Tes stats sont sauvegardées, les voici :")
    taux_reussite = (nb_victoires / nb_jeux_joues * 100) if nb_jeux_joues > 0 else 0
    print(Fore.YELLOW + f"⭐ Score : {score}")
    print(Fore.YELLOW + f"🎮 Parties jouées : {nb_jeux_joues}")
    print(Fore.YELLOW + f"🏆 Victoires : {nb_victoires}")
    print(Fore.YELLOW + f"📈 Taux de reussite : {taux_reussite:.2f}%")
else:
    score = 0
    nb_jeux_joues = 0
    nb_victoires = 0
    joueurs[prenom_utilisateur] = {"score": 0, "nb_jeux_joues": 0, "nb_victoires": 0}
    print(Fore.MAGENTA + f"\n✨ Bienvenue {prenom_utilisateur_original}! C'est ta première partie, bonne chance ! 🚀")

# Fonction lancer_jeu
def lancer_jeu(nb_essais_max, plafond, mode_nom, temps_limite=60):
    global score, nb_jeux_joues, nb_victoires
    nb_essais = 1
    r = random.randint(1,plafond)
    
    print(Back.CYAN + Fore.BLACK + f"\n 🎲 🌱 Mode {mode_nom} activé ! Devine un nombre entre 1 et {plafond} avec {nb_essais_max} essais maximum ! 💡" + Style.RESET_ALL)
    
    debut = time.time()  # démarrer le chrono

    while nb_essais <= nb_essais_max:
        temps_ecoule = time.time() - debut
        temps_restant = temps_limite - temps_ecoule

        if temps_restant <= 0:
            print(Fore.RED + f"\n⏰ Temps écoulé ! Tu avais {temps_limite}s pour trouver le nombre... Le nombre était {r} 💀")
            break

        print(Fore.CYAN + f"\n⌛ Temps restant : {int(temps_restant)} secondes")
        
        try:
            nb_utilisateur = int(input(Fore.YELLOW + f"\n👉 {prenom_utilisateur_original}, devine le nombre : " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "⚠️ Entrée invalide, entre un nombre !")
            continue

        if nb_utilisateur == r:
            print(Fore.GREEN + f"\n🎉 Bravo {prenom_utilisateur_original} ! Tu as trouvé le nombre {r} en {nb_essais} essais et {int(temps_ecoule)}s ! 🏆")
            score += 1
            nb_victoires += 1
            break
        elif nb_utilisateur < r:
            print(Fore.RED + "\n📈 C'est plus! Essaie avec un nombre plus grand ⬆️")
        elif nb_utilisateur > r:
            print(Fore.BLUE + "\n📉 C'est moins ! Essaie un plus petit nombre ⬇️")

        nb_essais += 1

    if nb_essais > nb_essais_max:
        print(Fore.RED + f" \n 💀 Oups! {prenom_utilisateur_original}... tu as épuisé tes essais ! Le nombre était {r} 🎯")
    
    nb_jeux_joues += 1
    taux_reussite = (nb_victoires / nb_jeux_joues) * 100
    
    print(Style.BRIGHT + Fore.CYAN + f"\n📊 Statistiques de {prenom_utilisateur_original} :")
    print(Fore.YELLOW + f"⭐ Score : {score}")
    print(Fore.YELLOW + f"🎮 Parties jouées : {nb_jeux_joues}")
    print(Fore.YELLOW + f"🏆 Victoires : {nb_victoires}")
    print(Fore.YELLOW + f"📈 Taux de reussite : {taux_reussite:.2f}%")
    
    # Sauvegarde après chaque partie (clé normalisée en lowercase)
    joueurs[prenom_utilisateur] = {
        "score": score,
        "nb_jeux_joues": nb_jeux_joues,
        "nb_victoires": nb_victoires
    }
    sauvegarder_donnees(joueurs)
    
    
# Boucle Principale
choix_continuer = "o"
while choix_continuer.lower() == 'o':
    print(Back.CYAN + Fore.LIGHTWHITE_EX + "\n === Choisis ton niveau de difficulté === 🏆" + Style.RESET_ALL)
    print(Fore.YELLOW + "\n 1️⃣ Facile (1-50, 10 essais) 🌱")
    print(Fore.YELLOW + "️2️⃣ Moyen (1-100, 7 essais) 🌱")
    print(Fore.YELLOW + "️3️⃣ Difficile (1-200, 5 essais) 🌱")

    try:
        choix_difficulte = int(input(("\n Entre le numéro de ton choix (1-3) 🎯 : ")))
    except ValueError:
        print(Fore.RED + "❌ Choix invalide, entre un nombre entre 1 et 3.")
        continue

    if choix_difficulte == 1:
        lancer_jeu(10,50, "Facile")
    elif choix_difficulte == 2:
        lancer_jeu(7,100, "Moyen", temps_limite=40)
    elif choix_difficulte == 3:
        lancer_jeu(5,200, "Difficile", temps_limite=20)
    else:
        print(Fore.RED + "❌ Choix invalide, essaie encore !")

    choix_continuer = input(Fore.MAGENTA + "\n Veux-tu continuer?(o:oui/n:non)" + Style.RESET_ALL)

# Message d' Aurevoir
if choix_continuer.lower() == "n":
    print(Fore.GREEN + f"\n👋 Merci d'avoir joué {prenom_utilisateur_original} ! Reviens vite pour plus de défis 🤩 !")
