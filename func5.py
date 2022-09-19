import matplotlib.pyplot as plt
import numpy as np

def f(x):
    d = (i**2 -2*i)/(i-2)
    return d 



x = []
y = []


for i in np.arange(-5, 5):
    x.append(i)
    y.append(f(i))
    
print(y)


fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()