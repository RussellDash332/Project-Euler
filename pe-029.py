power = {}

n = 100

for a in range(2,n+1):
    for b in range(2,n+1):
        power[a**b] = power.get(a**b,0)+1

print(len(power))
