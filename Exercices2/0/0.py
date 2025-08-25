# Je m'attends à  avoir 2 comme valeur de x en dehors
x = 2

def test():
    global x
    x += 1
    print(x)

test()
print(x)