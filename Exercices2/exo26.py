def fibonacci(n):

    fib_sequence = []

    
    if n <= 0:
        return fib_sequence 
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence.append(0)
    fib_sequence.append(1)

    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    return fib_sequence

n = 10
print(f"Les {n} premiers termes de la suite de Fibonacci : {fibonacci(n)}")