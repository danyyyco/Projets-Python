import re

# Regex pour numéro français (mobile ou fixe)
# - Format national : 0X XX XX XX XX
# - Format international : +33 X XX XX XX XX
pattern = re.compile(r"^(?:0[1-9](?:\s?\d{2}){4}|\+33\s?[1-9](?:\s?\d{2}){4})$")

def valider_numero(numero: str) -> bool:
    return bool(pattern.match(numero.strip()))

# Quelques tests
numeros = [
    "06 12 34 56 78",     # Valide
    "+33 6 12 34 56 78",  # Valide
    "01 23 45 67 89",     # Valide (fixe)
    "+33 1 23 45 67 89",  # Valide (fixe international)
    "0712345678",         # Valide (sans espaces)
    "+33612345678",       # Valide (sans espaces)
    "123456",             # Invalide
    "+331234567",         # Invalide
]

for num in numeros:
    print(f"{num:20} -> {'Valide ✅' if valider_numero(num) else 'Invalide ❌'}")
