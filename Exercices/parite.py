nombres = [1,2,3,4,5,6,7,8,9,10]

def isEven(x):
    if x % 2 == 0:
        return True
    elif x % 2 != 0:
        return False
    return None

def filterListEven(liste):
    for i in liste:
        if isEven(i):
            print(i)

filterListEven(nombres)
