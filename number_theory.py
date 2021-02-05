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

def fib(n):
    if n < 1:
        return 0
    else:
        a,b = 0,1
        for _ in range(n):
            a,b = b,a+b
        return a