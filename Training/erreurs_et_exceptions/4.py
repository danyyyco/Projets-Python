n1 = float(input("Entrer un nombre: "))
n2 = float(input("Entrer un nombre: "))

try:
    print(n1 / n2)
#except ZeroDivisionError as z:
    #print("Erreur: ", z)

except ZeroDivisionError:
    print("Erreur: Division par zero impossible")
