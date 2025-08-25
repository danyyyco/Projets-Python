heureTafSem = int(input("Combien d'heures travailles-tu par semaine? "))
salaire_brut_mensuel = float(input("Tu es payé combien par mois? "))

    # supposons que:
    # Il travaille 80h/sem et est payé 50000/mois
    # Il travaille 320h/mois puisque 80h * 4sem = 320h
    # Si pour 320h il obtient 50 000,
    # alors pour 1h il obtient combien?
    # On va faire 50 000 / 320

heureTafMois = heureTafSem * 4
print(type(heureTafSem))
print(type(heureTafMois))

salaire_horaire_brut = salaire_brut_mensuel / heureTafMois
print(type(salaire_brut_mensuel))
print(type(salaire_horaire_brut))
print(salaire_horaire_brut)
print(round(salaire_horaire_brut,2))