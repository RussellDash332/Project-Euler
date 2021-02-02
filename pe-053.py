count = 0
from choose import binom

for n in range(1,101):
    for r in range(n+1):
        check = binom(n,r)
        if (n,r) == (23,10):
            print("23C10 =",check)
        if check > 1000000:
            count += 1

print(count)