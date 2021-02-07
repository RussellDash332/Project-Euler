conc = ''
count = 0

while len(conc) <= 1000000:
    conc += str(count)
    count += 1

print(int(conc[1])*int(conc[10])*int(conc[100])*int(conc[1000])*int(conc[10000])*int(conc[100000])*int(conc[1000000]))