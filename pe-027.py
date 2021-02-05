import math

def exp(n,a,b):
    return n**2+a*n+b

def conc_prime(a,b):
    count = 0
    comp = 0 # composite indicator

    while comp < 1:
        for i in range(1,int(math.sqrt(exp(count,a,b)))+1):
            if exp(count,a,b) % (i+1) == 0:
                comp += 1
        count += 1
    return (count-1)

max_cp = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        if a**2-4*b <= 0 and conc_prime(a,b) > max_cp:
            max_cp = conc_prime(a,b)
            print(f"a = {a}, b = {b}, ab = {a*b}, primes = {max_cp}")