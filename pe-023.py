## The code might take a while.

from number_theory import sum_factor

proper_factor = lambda x: sum_factor(x)-x

limit = 28123

abundant = []
for i in range(limit+2):
    if proper_factor(i+1) > (i+1):
        abundant.append(i+1)

#print(abundant) ## abundant is still sorted in this point

sum_abundant = {}

for j in range(len(abundant)):
    for k in range(j,len(abundant)):
        test = abundant[j]+abundant[k]
        if test <= limit:
            sum_abundant[test] = sum_abundant.get(test,0)+1
sum_abundant = sorted(list(sum_abundant.keys()))

#print(sum_abundant) ## list of numbers that can be expressed as sum of 2 AN

# 28123 is the sum of 2 abundant numbers, the long number below is basically sum of all integers from 1 to 28123, inclusive
ans = 395465626 - sum(sum_abundant)
print(ans)