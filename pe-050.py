# The code might take a while.

from check_primes import sieve

primes = sieve(1000000)[1]

length = 0 # length of the longest chain
answer = 0

bound = len(primes)

for i in range(len(primes)):
    for j in range(i+length, bound): # given current maximum length, we can check whether we can improve our bound
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                answer = sol
        else:
            bound = j+1
            break

print("Answer:",answer)
