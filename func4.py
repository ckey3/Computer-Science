

def f(x):
    return x**2 / 4

def g(x):
    return 2*(x**.5)

n = 2

print("starting value = ", n)
b = f(n)
print(f'f({n}) = {b}')


c = g(b)
print("g(b) =", c)
if n == c:
    print("functions are inverse")
else:
    print("not a inverse of the function")

