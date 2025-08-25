n = int(input("Enter a number: "))
f=0

while n > 1:
    f = f*n*n-1
    n-=2
print(f)