import matplotlib.pyplot as plt
import numpy as np


def slope(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    try:
        m = dy/dx
    except:
        m = None
    return m


def yint(x1,y1,x2,y2):
    b = -slope(x1,y1,x2,y2)*x2+y2
    return b


s = slope(2,5,4,10)
print(s)
b = yint(2,5,4,10)



xa = []
ya = []

for i in range(-10,11):
    xa.append(i)
    ya.append(s*i+b)

print(xa,ya)

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()