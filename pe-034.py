from number_theory import factorial

count = 3
curious = []

while count <= 400000: # set a high limit because any number above this will not satisfy
    split = str(count)
    check = 0
    for i in range(len(split)):
        check += factorial(int(split[i]))
        
    if count == check:
        curious.append(count)
    count += 1

print(curious)
print(sum(curious))