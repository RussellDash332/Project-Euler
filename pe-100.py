# n^2 + (2m-1)n - m(m-1) = 0
# D = 8m^2 - 8m + 1 = k^2 -> 8m^2 - 8m + (1-k^2) = 0
# D2 = 32(k^2 + 1) = p^2 -> 2(k^2 + 1) = q^2 -> k^2 + 1 = 2r^2 -> k^2 - 2r^2 = -1 -> PELL
# Suppose a solution for k is found, then
# m = (2 + sqrt(2k^2 + 2))/4
# n = (1-2m+k)/2 = (-sqrt(2k^2 + 2)/2+k)/4

def f(k): # k is a solution to k^2 - 2r^2 = -1
    s = round((2*k**2 + 2)**0.5)
    m, n = (2 + s) // 4, (2*k - s) // 4
    return m, n

t = 1
while True:
    m, n = f(round((1+2**0.5)**t + (1-2**0.5)**t)//2)
    if m + n > 10**12:
        print(m)
        break
    t += 2