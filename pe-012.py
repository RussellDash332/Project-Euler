from number_theory import factor

n = 1

def triangle_factor(n):
    if n % 2:
        return factor(n)*factor((n+1)//2)
    else:
        return factor(n+1)*factor(n//2)

while triangle_factor(n) < 500:
    n += 1

print(n*(n+1)//2)