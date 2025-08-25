import os
from os import removedirs

chemin = r"C:\Users\dimit\Documents\os"

nouveau_dossier = os.path.join(chemin, 'audios', 'audios-trend')
#print(nouveau_dossier)

if not os.path.exists(nouveau_dossier):
    os.makedirs(nouveau_dossier)

   #os.makedirs(nouveau_dossier, exist_ok=True)

if os.path.exists(nouveau_dossier):
    removedirs(nouveau_dossier)