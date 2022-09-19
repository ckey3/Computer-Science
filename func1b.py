import matplotlib.pyplot as plt


def f(x):
    y = (x**2)/4
    return y 

def d(x):
    y2 = 2*(x**.5)
    return y2

x = []
y = []
y2 = []

for i in range(0, 11):
    x.append(i)
    y.append( f(i) )
    y2.append( d(i) )

print("x: ", x)
print("y: ", y)
print("y2: ",y2)

fig, ax = plt.subplots()
ax.plot(x, y, y2)

plt.show()