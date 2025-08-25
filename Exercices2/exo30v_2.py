import random
import time
from colorama import init, Fore, Back, Style

# Initialiser colorama avec reset automatique
init(autoreset=True)

# Initialisation des statistiques du joueur
score = 0
games_played = 0
games_won = 0
choix = "o"

# Demander le nom du joueur
print(Back.BLUE + Fore.LIGHTWHITE_EX + Style.BRIGHT + "=== Bienvenue au jeu de devinette ! === 🎉\n")
player_name = input(Fore.CYAN + Style.BRIGHT + "Quel est ton prénom, aventurier ? 🎮 : " + Style.RESET_ALL)

print(Back.MAGENTA + Fore.LIGHTWHITE_EX + Style.BRIGHT + f"\nSalut {player_name} ! 🚀 Prépare-toi à une aventure pleine de mystère et de chiffres secrets ! 🔢✨\n" + Style.RESET_ALL)

# Petite pause immersive
time.sleep(1)

# Fonction pour choisir le niveau de difficulté
def choisir_difficulte():
    print(Back.CYAN + Fore.LIGHTWHITE_EX + "=== Choisis ton niveau de difficulté === 🏆" + Style.RESET_ALL)
    print(Fore.YELLOW + "1️⃣  Facile (1-50, 10 essais) 🌱")
    print(Fore.YELLOW + "2️⃣  Moyen (1-100, 7 essais) ⚔️")
    print(Fore.YELLOW + "3️⃣  Difficile (1-200, 5 essais) 🔥")

    while True:
        try:
            niveau = int(input(Fore.MAGENTA + "Entre le numéro de ton choix (1-3) 🎯 : " + Style.RESET_ALL))
            if niveau == 1:
                return (50, 10, "🌱 Mode Facile")
            elif niveau == 2:
                return (100, 7, "⚔️ Mode Moyen")
            elif niveau == 3:
                return (200, 5, "🔥 Mode Difficile")
            else:
                print(Fore.RED + "❌ Choix invalide, essaie encore !")
        except ValueError:
            print(Fore.RED + "⚠️ Entre un nombre valide !")

# Boucle principale du jeu
while choix.lower() == "o":
    games_played += 1
    max_nombre, max_essais, mode_nom = choisir_difficulte()
    r = random.randint(1, max_nombre)
    nb_essais = 0

    print(Back.CYAN + Fore.BLACK + f"\n🎲 {mode_nom} activé ! Devine un nombre entre 1 et {max_nombre} avec {max_essais} essais maximum ! 💡" + Style.RESET_ALL)

    while nb_essais < max_essais:
        try:
            nb_utilisateur = int(input(Fore.YELLOW + f"👉 {player_name}, devine le nombre : " + Style.RESET_ALL))

            if nb_utilisateur == r:
                print(Fore.GREEN + f"🎉 Bravo {player_name} ! Tu as trouvé le nombre {r} en {nb_essais + 1} essais ! 🏆")
                score += 1
                games_won += 1
                break
            elif nb_utilisateur > r:
                print(Fore.RED + "📉 Trop haut ! Essaie un plus petit nombre ⬇️")
            elif nb_utilisateur < r:
                print(Fore.BLUE + "📈 Trop bas ! Essaie un plus grand nombre ⬆️")

            nb_essais += 1

        except ValueError:
            print(Fore.RED + "⚠️ Ce n'est pas un nombre valide ! 🔢")

    if nb_essais == max_essais and nb_utilisateur != r:
        print(Fore.RED + f"💀 Oups {player_name}... tu as épuisé tes essais ! Le nombre était {r} 🎯")

    # Statistiques du joueur
    taux_reussite = (games_won / games_played) * 100 if games_played > 0 else 0
    print(Style.BRIGHT + Fore.CYAN + f"\n📊 Statistiques de {player_name} :")
    print(Fore.YELLOW + f"⭐ Score : {score}")
    print(Fore.YELLOW + f"🎮 Parties jouées : {games_played}")
    print(Fore.YELLOW + f"🏆 Victoires : {games_won}")
    print(Fore.YELLOW + f"📈 Taux de réussite : {taux_reussite:.2f}%\n")

    choix = input(Fore.MAGENTA + "🔄 Veux-tu rejouer ? (o/n) : " + Style.RESET_ALL)
    if choix.lower() == "n":
        print(Fore.GREEN + f"\n👋 Merci d'avoir joué {player_name} ! Reviens vite pour plus de défis 🤩 !\n")
