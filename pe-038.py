count = 1
num = [str(i) for i in range(1,10)]

cp = []

while count < 1000000:
    for n in range(9):
        conc_prod = ''
        pandig = 0

        for i in range(n+1):
            conc_prod += str(count*(i+1))

        if len(conc_prod) == 9: # checks pandigitality
            for i in range(9):
                if num[i] in list(conc_prod):
                    pandig += 1
        
        if pandig == 9:
            cp.append(int(conc_prod))
    count += 1

print(cp)
print("Answer:",max(cp))
