#input 2 points (x1,y1) and (x2,y2)
#output slope of line between the points


x1 = float(input("x1:"))
x2 = float(input("x2:"))
y1 = float(input("y1:"))
y2 = float(input("y2:"))



slope = (y2 - y1)/(x2 - x1)

#y-intercept
b = y1 - (slope*x1)

#x-intercpet

x = -(y1/slope) + x1

print("x-intercept =",x)
print("y-intercept =",b)
print("slope =",slope)