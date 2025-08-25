def operations(x,y,signe):
    def addition():
        return operations(x,y)
    def soustraction():
        return operations(x,y)
    if signe == "+":
         return addition
    else:
        return soustraction
    
r1 = operations(2,3,"+")
print(r1)