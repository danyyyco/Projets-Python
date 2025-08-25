# for i in range(5):
#     print("Tour", i)

# for i in range(1,6):
#     print("Tour", i)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# for i in range(10):
#     if i == 5:
#         break    # quitte la boucle
#     if i % 2 == 0:
#         continue # saute le tour si pair
#     print(i)

# for lettre in "Python":
#     print(lettre)

# for fruit in ["pomme", "banane", "mangue"]:
#     print(fruit)

# n = int(input("Entrez un nombre: "))
# s = 0

# for i in range(1, n + 1):
#     s += i  # Ajoute la valeur de i à s
#     print(f"{s - i} + {i} = {s}")  # Affiche la somme précédente + i = somme actuelle

import random

secret = random.randint(1, 100)
tentative = 0
nbTentative = 5

while tentative != secret and nbTentative!=0:
    nbTentative-=1
    tentative = int(input("Devine le nombre : "))
    if(tentative>secret):
        print("Trop grand")
    elif(tentative<secret):
        print("Trop petit")
    else:
        print("Eureka")

# for i in range(1, 6):
#      print("*" * i)

# fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

# for fruit in fruits:
#     print(fruit)
# else:
#     print('Plus de fruits dans le panier') 


# for i in range(3):
#     print(i)

# prenom = "John"
# for lettre in prenom:
#     print(lettre)

# for (pk, name) in [(1, "Patrick"), (2, "John"), (3, "Marie")]:
#     print(pk, name)


# fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']
# fruits_manges = 0

# for fruit in fruits:
#     print("Je mange des " + fruit)
#     fruits_manges += 1
#     if fruits_manges == 3:
#         break

# print("Je n'ai plus faim !")



# for a in range(5):
#     for b in range(5):
#         print("a:", a, "b: ", b)
#         if b == 3:
#             break


# i = 0
# while i < 10:
#     print('Salut')
#     i += 1


# i = 0
# while i < 3:
#     print('Salut')
#     i += 1
# else:
#     print('Au revoir')


# fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

# for fruit in fruits:
#     if fruit == '🍒':
#         print('Pas fan des cerises')
#         continue

#     print(fruit)

# print('On passe à la suite')
