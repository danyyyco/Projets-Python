somme = 0
difference = 0
division = 0
multi = 0
# choix = 'oui'
choix = ''

while (choix!= 'non'):
    print('=== CALCULATRICE ===\n')
    print('1-Addition')
    print('2-Soustraction')
    print('3-Multiplication')
    print('4-Division')
    op = int(input('\nQuelle opération souhaitez-vous faire? '))
    nb1 = int(input('Entrez un nombre: '))
    nb2 = int(input('Entrez un second nombre: '))

    if(op==1):
        somme = nb1 + nb2
        print(f"La somme de {nb1} et {nb2} est de: {somme}")
    elif(op==2):
        difference = nb1 - nb2
        print(f"La différence de {nb1} et {nb2} est de: {difference}")
    elif(op==3):
        multi = nb1 * nb2
        print(f"La multiplication de {nb1} et {nb2} est de: {multi}")
    else:
        division = nb1 / nb2
        print(f"La division de {nb1} et {nb2} est de: {division}")

    choix = input("Voulez-vous continuer? oui/non: ")
    if choix == 'non':
        print('Au revoir')