# Formula obtained from the quadratic formula

def is_triangle(n):
    return (-1+(8*n+1)**0.5) % 2 == 0

def is_square(n):
    return n**0.5 % 1 == 0

def is_pentagonal(n):
    return (1+(24*n+1)**0.5) % 6 == 0

def is_hexagonal(n):
    return (1+(8*n+1)**0.5) % 4 == 0

def is_heptagonal(n):
    return (3+(40*n+9)**0.5) % 10 == 0

def is_octagonal(n):
    return (1+(3*n+1)**0.5) % 3 == 0