a = 5
b = 2

try:
    resultat = a / b
except ZeroDivisionError:
    print("Division par zero impossible.")
except TypeError:
    print ("La variable b n'est pas du bon type.")
# except NameError:
#     print("La variable b n'est pas définie")
except NameError as e:
    print("Erreur:", e)
else:
    print (resultat)
finally:
    print("Fin du bloc")