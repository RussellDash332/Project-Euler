def is_triangle(n):
    return (-1+(8*n+1)**0.5) % 2 == 0
      
def is_pentagonal(n):
    return (1+(24*n+1)**0.5) % 6 == 0
      
def is_hexagonal(n):
    return (1+(8*n+1)**0.5) % 4 == 0