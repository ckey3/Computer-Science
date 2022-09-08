n = input("Enter your name:")

#len counts the length
lenght = len(n)

print(lenght)

if lenght < 6:
    print(f"{n}, your name is short")
else:
    print(f"Your name is not short {n}. It has {lenght} letters.")
