import matplotlib.pyplot as plt
from cmath import sin
import numpy as np

x = []
y = []


#loop
for i in np.arange(0, 11, .1):
    f = sin(i)
    x.append(i)
    y.append(f) #add to array
    
print(y)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()