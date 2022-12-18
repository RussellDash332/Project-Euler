coords = open('resources/p102_triangles.txt', 'r').readlines()

def area(x1, y1, x2, y2, x3, y3):
    return 0.5*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

cont = 0
for line in coords:
    x1, y1, x2, y2, x3, y3 = map(int, line.split(','))
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x1, y1, x2, y2, 0, 0)
    A2 = area(x1, y1, 0, 0, x3, y3)
    A3 = area(0, 0, x2, y2, x3, y3)
    cont += A == A1 + A2 + A3
print(cont)