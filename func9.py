



def slope(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    try:
        m = dy/dx
    except:
        m = None
    return m


s = slope(2,5,2,10)

print(s)



