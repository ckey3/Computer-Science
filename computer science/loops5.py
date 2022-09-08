#initialize
f1 = 1
f2 = 1
print(f1)
print(f2)

for i in range(2,31):
    f_new = f1 + f2
    print(f_new)

#update section
    f1 = f2
    f2 = f_new