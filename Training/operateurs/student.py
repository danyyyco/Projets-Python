def calculer_moyenne(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def est_admis(moyenne, seuil_moyenne, seuil_note):
    return moyenne >= seuil_moyenne and n1 >= seuil_note and n2 >= seuil_note and n3 >= seuil_note

# Saisir les notes de l'étudiant
n1 = float(input("Entrez la première note : "))
n2 = float(input("Entrez la deuxième note : "))
n3 = float(input("Entrez la troisième note : "))

# Définir les seuils
seuil_moyenne = 10.0  # Par exemple, la moyenne requise pour être admis
seuil_note = 8.0      # Par exemple, la note minimale requise

# Calculer la moyenne
moyenne = calculer_moyenne(n1, n2, n3)

# Vérifier si l'étudiant est admis ou refusé
if est_admis(moyenne, seuil_moyenne, seuil_note):
    print(f"L'étudiant est admis avec une moyenne de {moyenne:.2f}.")
else:
    print(f"L'étudiant est refusé avec une moyenne de {moyenne:.2f}.")
