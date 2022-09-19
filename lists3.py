#find lowest value of costs

costs = [10.00, 18.00 ,18.00, 11.00, 17.50, 11.00, 17.50, 11.00, 17.50, 11.00, 30.00, 17.50, 20.50, 11.50, 6.50, 5.60, 7.50]

lowVal = 999

#is maxVal greater then i if is become maxVal
for i in costs:
    if i < lowVal:
        lowVal = i

print(f"Lowest =  {lowVal}")