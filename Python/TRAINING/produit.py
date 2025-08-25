nom = input("Entrez le nom du produit: ")
prix = float(input("Entrez le prix: "))
quantite = int(input("Entrez la quantité: "))
est_en_promo = input("Est-il en promo? (oui/non): ")

while est_en_promo != 'oui' and est_en_promo != 'non':
    est_en_promo = input("Réponse invalide. Est-il en promo? (oui/non): ")

total_en_stock = prix * quantite

print(f"\nNom du produit: {nom}\n")
print(f"Prix unitaire: {prix} FCFA\n")
print(f"Quantité: {quantite}\n")
print(f"En promotion: {est_en_promo}\n")
print(f"Valeur totale du stock: {total_en_stock} FCFA \n")