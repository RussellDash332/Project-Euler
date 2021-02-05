def gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x

def lcm(x, y):
    return x*y//gcd(x,y)

def factorial(n):
    if n < 2:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result *= i
    return result