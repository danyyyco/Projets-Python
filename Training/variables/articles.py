price_article = float(input("Enter the article price: "))
quantity_article = int(input("Enter the article quantity: "))

price_HT = price_article * quantity_article
tva = price_HT * (20/100)
ttc = price_HT + tva

print(f"{price_HT:.2f}")
print(f"{tva:.2f}")
print(f"{ttc:.2f}")