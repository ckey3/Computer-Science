
class line:
    def __init__(self,m,b):
        self.slope = m 
        self.yintercept = b
        self.xintercept = -b/m 

    def y(self,x):
        yval = self.slope*x + self.yintercept
        return yval

    def x(self,y):
        xval = (y - self.yintercept) / self.slope
        return xval


#end of line class
line1 = line(2,3) #slope of (2.3)

print(line1.slope)
print(line1.xintercept)
print(line1.y(5))
print(line1.x(13))