"""sentence = input("Enter a sentence: ")
print(len(sentence))
print(sentence.upper())
print(sentence.lower())"""


"""name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(f"Hello, {surname} D{name}")"""


"""strg = "   Hello World    "
print(strg.strip())"""


"""sentence = input("Enter a sentence: ")
letter = input("Enter a letter to search: ")
print(sentence.find(letter)) #Affiche l'index du premier a trouvé (a est un exemple)
print(sentence.index(letter)) # Fais la même chose
print(sentence.count(letter))"""


"""strg = "Hello world!"
reverse_strg1 = strg[::-1]
reverse_strg2 = reversed(strg)
reverse_strg_reverse = reverse_strg1[::-1]
print(reverse_strg1)
print(reverse_strg2)
print(reverse_strg_reverse)"""


"""st = "Hello world"
words = st.split()
words_reverse = words[::-1]
st_reverse = " ".join(words_reverse)
print(words)
print(words_reverse)
print(st_reverse)"""

"""import datetime
nom = "Martins"
prenom = "Jack"
matricule = 103
score_performance = 50.250
date = datetime.date.today()
print(f"Nom: {nom}\nPrenom: {prenom}\nMatricule: {matricule}\nScore de performance: {score_performance:.2f}\nDate du rapport: {date.strftime('%d/%m/%Y')}")"""

import re


def extraire_texte_html(chaine):
    # Utilisation d'une expression régulière pour extraire le texte entre les balises HTML
    pattern = r'>s*(.*?)s*<'
    resultats = re.findall(pattern, chaine)

    # Joindre les résultats extraits en une seule chaîne
    texte_extrait = ' '.join(resultats)

    return texte_extrait


# Exemple de chaîne avec des balises HTML
chaine_html = "<p>Ceci est un <b>paragraphe</b>.</p> <div>Voici un autre <i>exemple</i>.</div>"

# Extraction du texte
texte = extraire_texte_html(chaine_html)
print(texte)
