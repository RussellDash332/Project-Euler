def npf(number): # number of prime factors
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

j = 2*3*5*7
while True:
    if npf(j) == 4 and npf(j+1) == 4 and npf(j+2) == 4 and npf(j+3) == 4:
        print(j)
        break
    j += 1