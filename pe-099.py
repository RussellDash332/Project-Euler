from math import log
exps = []
for l in open('resources/p099_base_exp.txt', 'r').readlines():
    a, b = map(int, l.split(','))
    exps.append((len(exps) + 1, a, b))
print(max(exps, key=lambda x: x[2]*log(x[1]))[0])