# chemin = r"C:\Users\dimit\Documents\texte.txt"
# with open (chemin, "r", encoding="utf-8") as f:
#     contenu = f.readlines()
#     for num,cont in enumerate(contenu):
#         print(f"\n{num}:{cont}\n")
        
# chemin = r"C:\Users\dimit\Documents\article.txt"
# with open (chemin, "r", encoding="utf-8") as f:
#     contenu = f.read()
#     mots = contenu.split()
#     nb_mots = len(mots)
#     print(nb_mots)

chemin1 = r"C:\Users\dimit\Documents\source.txt"
chemin2 = r"C:\Users\dimit\Documents\destination.txt"

with open (chemin1, "r", encoding="utf-8") as f:
    contenu = f.read()
    print(contenu)
    
with open(chemin1, "a+") as f:
    texto = "\nHey boss"
    f.write(texto)
    f.seek(0)
    nouv_cont = f.read()
    print(nouv_cont)
    
with open(chemin2, "w") as f:
    # f.write(contenu)
    f.write(nouv_cont)
    
with open (chemin2, "r", encoding="utf-8") as f:
    contenu2 = f.read()
    print(contenu2)