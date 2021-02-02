def digital_sum(a,b):
    n = 1
    for _ in range(b):
        n *= a
    n = list(map(int,str(n)))
    return sum(n)

result = 0
for a in range(1,100):
    for b in range(1,100):
        result = max(digital_sum(a,b),result)

print(result)