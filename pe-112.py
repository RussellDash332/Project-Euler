def bouncy(n):
    s = str(n)
    inc = any([a < b for a, b in zip(s, s[1:])])
    dec = any([a > b for a, b in zip(s, s[1:])])
    return inc and dec

b = 0
n = 100
perc = 99
while 100*b != perc*(n-1):
    b += bouncy(n)
    n += 1
print(n-1)