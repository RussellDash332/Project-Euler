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
    count, i = 0, 1
    while i * i <= n:
        if n % i == 0:
            count += 2
            if i * i == n:
                count -= 1
        i += 1
    return count

def sum_factor(n):
    ans, i = 0, 0
    while i * i <= n:
        if n % i == 0:
            ans += i + n // i
            if i * i == n:
                ans -= i
        i += 1
    return count

def fib(n):
    if n < 1:
        return 0
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
