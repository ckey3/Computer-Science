


def q1(x):
    y = 2*x**2 + x - 2
    return y

#x = 5
#print( q1(x) )

#loop
#for i in range(5):
 #   x = input("Enter a number: ")
  #  n = float(x) number without decimal
   # print(x)
    #print( q1(n) )

doAgain = True

while doAgain:#while statement is for when you stop
    x = input("Enter a number: ")
    if x == "stop":
        doAgain = False
        print("done")
    else:
        n = float(x)
        print( q1(n) )



