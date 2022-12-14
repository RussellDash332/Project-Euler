# Problem 71: see? it's useful!
def farey(n, tx, ty):
    it = 0
    x1, y1, x2, y2 = 0, 1, 1, n
    while (x2, y2) != (tx, ty):
        it += 1
        c = (y1 + n) // y2
        x1, x2, y1, y2 = x2, c * x2 - x1, y2, c * y2 - y1
    return it

n = 12000
print(farey(n, 1, 2) - farey(n, 1, 3) - 1)