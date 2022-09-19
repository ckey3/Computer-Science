import matplotlib.pyplot as plt
import numpy as np

def f(x):
    dx = 0.000000000001
    try:
        y = 3/(x-2)
    except:
        y = (f(x+dx) + f(x-dx)) / 2
    return y 

def lim(x):
    y = x
    return y 

x=-5

xa = []
ya = []



for i in range(-10,10):
    xa.append(i)
    ya.append(f(i))
    print(i,f(i))

print(xa,ya)

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()