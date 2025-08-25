def filtrer_liste(liste, condition):
    return [element for element in liste if condition(element)]

nombres = [1, 2, 3, 4, 5, 6]
pairs = filtrer_liste(nombres, lambda x: x % 2 == 0)
print("Nombres pairs :", pairs) 

mots = ["chat", "chien", "o", "maison", "arbre"]
mots_long = filtrer_liste(mots, lambda x: len(x) > 3)
print("Mots de plus de 3 lettres :", mots_long)

nombres_sup_3 = filtrer_liste(nombres, lambda x: x > 3)
print("Nombres supérieurs à 3 :", nombres_sup_3)
