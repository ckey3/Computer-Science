import matplotlib.pyplot as plt
import numpy as np

def f(x):
    dx = 0.000000000000001
    try:
        y = (x**2 - 2*x)/(x-2)
    except:
        y = (f(x+dx) + f(x-dx)) / 2
    return y 

def lim(x):
    y = x
    return y 

x=2

xa = []
ya = []



for i in range(-5, 5):
    ya.append(f(i))
    xa.append(i)
    print(i,f(i))

print(xa,ya)

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()
