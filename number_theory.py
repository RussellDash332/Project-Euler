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

def factor(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

def sum_factor(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer