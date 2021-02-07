answer = 0
for i in range(1,1001):
    add = 1
    for j in range(i):
        add = (add*i) % (10**10)
    answer = (answer + add) % (10**10)

print(answer)