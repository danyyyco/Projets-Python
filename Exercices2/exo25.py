def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:  # la valeur de i change à chaque iteration. ça varie entre 2 et 10 n reste toujours à 11 vu que aucun entier entre 2 et 10 ne divise 11 alors 11 est premier 11 est un exemple
            return False
    return True


print(est_premier(11))
print(est_premier(10))
