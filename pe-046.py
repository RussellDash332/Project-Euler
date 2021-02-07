from check_primes import is_composite
import math

bigger_flag = False
i = 3

while not bigger_flag:
    if is_composite(i) and i % 2 == 1:
        goldbach = False
        for j in range(2,i):
            flag = False
            for k in range(1,int(math.sqrt(i//2))+1):
                if not is_composite(j)and j + 2*k**2 == i:
                    goldbach = True
                    print('%d = %d + 2 x %d^2'%(i,j,k))
                    flag = True
                    break
            if flag:
                break # just continue with the next i if we found one combination
        if not goldbach:
            bigger_flag = True
    i += 1
print()
print("Asnwer:",i-1)