from number_theory import gcd

e = [2]
for k in range(33):
    e.extend([1, 2*k+2, 1])
s2 = [1] + [2]*99

def get_frac(n, t):
    n = n[:t][::-1]
    a, b = n[0], 1
    for i in range(1, t):
        a, b = b, a
        a += b*n[i]
    d = a // gcd(a, b)
    return (d, sum(map(int, str(d))))

print(get_frac(e, 100))