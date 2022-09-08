#distance between two points given two x-values and a funtion


def f1(x):
    y = 2*(x)+3
    return y

#Inputs
x1, x2 = 1, 5

#Funtions
y1 = f1(x1)
y2 = f1(x2)

#calculate distance
dx = x2 - x1
dy = y2 - y1
distance = (dx**2 + dy**2)**0.5

#slope
m = dy/dx
print(m)

#Output
print("Distance = ", distance)


#quadratic function f(x) = (2x)^2 + 3x + 4
def f2(x):
    q = 2*(x)**2 + 3*x + 4
    return q

#Inputs
x3, x4 = 1, 5

#Funtions
y3 = f2(x3)
y4 = f2(x4)

#calculate distance
dx2 = x4 - x3
dy2 = y4 - y3
distance2 = (dx2**2 + dy2**2)**0.5

#Output
print("quad Distance = ", distance2)
