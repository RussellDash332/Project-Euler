from number_theory import sum_factor

amicable = []
limit = 10000

for i in range(1,limit):
    j = sum_factor(i)-i
    if sum_factor(j) == i+j and j < limit and i != j:
        amicable.append(i)
        amicable.append(j)

# print(sorted(amicable)[::2])
print(sum(amicable)//2)