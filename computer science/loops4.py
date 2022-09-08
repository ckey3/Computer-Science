n = 25
#isPrime = True
for i in range(2, n):
    print(n, i,n%i)
    if n%i == 0:
        print("Not a prime")
        #isPrime = False
        break
else:
    print("is prime")

# if isPrime == True:
#     print("is prime")
