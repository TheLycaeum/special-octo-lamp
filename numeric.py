def add(x, y):
    for _ in range(y):
        x += 1
    return x
        
def sub(x, y):
    for _ in range(y):
        x -= 1
    return x


def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero")
    q = 0
    while x >= y:
        q += 1
        x = x - y
    return q
