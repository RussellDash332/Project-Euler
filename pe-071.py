# No, this is suboptimal but good to have
def farey(n, tx, ty):
    x1, y1, x2, y2 = 0, 1, 1, n
    while (x2, y2) != (tx, ty):
        c = (y1 + n) // y2
        x1, x2, y1, y2 = x2, c * x2 - x1, y2, c * y2 - y1
    return x1, y1

a, b = 3, 7
y, x = 5, 2
dm = 10**6

# ay-bx = 1
while y <= dm - b:
    y += 7
    x += 3
    # (x/y) < (x+3)/(y+7) < (3/7)
print(x)