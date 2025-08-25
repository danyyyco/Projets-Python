class MonErreur(Exception):
    pass

def fonction():
    raise MonErreur("Ceci est une erreur personnalisée.")

try:
    fonction()
except MonErreur as e:
    print("Erreur capturée :", e)
