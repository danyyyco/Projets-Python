def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    else:
        return False

annee = int(input("Entrez une année : "))

if est_bissextile(annee):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")
