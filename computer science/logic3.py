x = input("what size drink do you want?")



#can put lower or upercase letters(case insensitive)
x = x.lower()
#can put spaces at begining or end(remove whitespace)
x = x.strip()
#can put space in the middle of a word
x = x.replace(" ", "")

#x = x.lower().strip().replace(" ", "")

if x == "venti":
    print(f"you should have a smaller size")
elif x == "tall":
    print(f"Do you mean small?")
elif x == "grande":
    print(f"Nice")
else:
    print(f"What do you mean?")

