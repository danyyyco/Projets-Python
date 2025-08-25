secondes = int(input("Enter a number of seconds: "))

toMinutes = secondes // 60
toSeconds = secondes % 60

print(f"{secondes} secondes = {toMinutes:02}:{toSeconds:02}")
print(f"{secondes} secondes = {toMinutes} minutes {toSeconds} secondes")