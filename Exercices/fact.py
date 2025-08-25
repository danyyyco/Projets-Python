n = int(input("Enter a number: "))

def fact(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m * fact(m-1)

print(fact(n))