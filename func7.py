import matplotlib.pyplot as plt
import numpy as np

def f(x):
    dx = 0.00000001
    try:
        y = (x**3 + 125) / (x + 5)
    except:
        y = (f(x+dx) + f(x-dx)) / 2
    return y 

def lim(x):
    y = x
    return y 

x=-5

xa = []
ya = []



for i in range(-10, 10):
    ya.append(f(i))
    xa.append(i)
    print(i,f(i))

print(xa,ya)

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()