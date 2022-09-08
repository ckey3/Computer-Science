from cmath import pi



r = float(input("Radius:"))
h = float(input("Hight:"))

V = (pi*h**2)*r


if V > 1000:
    print(f"{V} is greater than 1 liter")
else:
    print(f"{V} is less than 1 liter")
