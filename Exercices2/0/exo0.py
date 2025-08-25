def operations(x, y, signe):
    def addition():
        return x + y
    def soustraction():
        return x - y
    def multiplication():
        return x * y
    def division():
        return x / y
    if signe == "+":
        return addition()
    elif signe == "-":
        return soustraction()
    elif signe == "*":
        return multiplication()
    else:
        return division()

r1 = operations(2, 3, "-")
print(r1)