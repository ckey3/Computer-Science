import matplotlib.pyplot as plt

offset = 0.001
diff = 1
g = 2
target = 25

test = g * g
g = (g + (target/g))/2

#itteration
#test = g * g
#g = (g + (target/g))/2

#test = g * g
#g = (g + (target/g))/2

while diff > offset:
    g = (g + (target/g))/2
    test = g * g
    diff = abs(target - test)

print(g)