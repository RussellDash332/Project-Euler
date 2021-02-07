# Currently not changing anything from the old code.
import itertools
from check_primes import is_prime

def pandipri(n):
    panpri = []

    num = [] # all 1-digit numbers from 1 to n
    int_num = []
    for i in range(n):
        num.append(str(i+1))
        int_num.append(i+1)

    perm = list(itertools.permutations(int_num))

    perm_list = []
    for i in range(len(perm)):
        joined = ''
        for j in range(n):
            joined += str(perm[i][j])
        perm_list.append(int(joined))

    for count in range(len(perm_list)): # DUMMY COMMAND
        pan = 0
        for i in range(len(num)):
            if num[i] in list(str(perm_list[count])):
                pan += 1

        if pan == n and is_prime(perm_list[count]):
            panpri.append(perm_list[count])

    if panpri:
        print(f"{n} digits: {panpri[-1]}")
    else:
        print(f"{n} digits: No solution")

for i in range(9):
    pandipri(i+1)
