import matplotlib.pyplot as plt


x = []
y = []


#loop
for i in range(21):
    f = i**2-3*i+4
    x.append(i)
    y.append(f) #add to array
    
print(y)
fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()