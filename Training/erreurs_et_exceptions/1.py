try:
    # Code qui peut causer une exception
    x = 1 / 0
except ZeroDivisionError as e:
    print("Une erreur est survenue :", e)
    raise  # Relance l'exception ZeroDivisionError

