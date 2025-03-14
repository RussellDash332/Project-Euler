GO = 0
CC = {2, 17, 33}
CH = {7, 22, 36}
nextR = {7: 15, 22: 25, 36: 5}
nextU = {7: 12, 22: 28, 36: 12}
JAIL = 10
G2J = 30
R1 = 5
R2 = 15
R3 = 25
R4 = 35
U1 = 12
U2 = 28
C1 = 11
E3 = 24
H2 = 39

from random import *; from collections import *
def sim(n):
    A = [0]*40; T = 10**7
    cc = [GO, JAIL]+[-1]*14; shuffle(cc); cc = deque(cc)
    ch = [GO, JAIL, C1, E3, H2, R1, -1, -1, -2, -3]+[-4]*6; shuffle(ch); ch = deque(ch)
    pos = GO; doubles = 0
    for _ in range(T):
        d1 = randint(1, n); d2 = randint(1, n)
        if d1 == d2: doubles += 1
        else: doubles = 0
        if doubles == 3: pos = JAIL; doubles = 0
        else:
            pos = (pos+d1+d2)%40
            if pos == G2J: pos = JAIL
            while pos in CC or pos in CH:
                if pos in CC:
                    x = cc.popleft(); cc.append(x)
                    if x != -1: pos = x
                    else: break
                elif pos in CH:
                    x = ch.popleft(); ch.append(x)
                    if x == -3:   pos = (pos-3)%40
                    elif x == -1: pos = nextR[pos]
                    elif x == -2: pos = nextU[pos]
                    elif x != -4: pos = x
                    else: break
        A[pos] += 1
    return [i/T*100 for i in A]
res = sim(4)
print(''.join(t for _, t in sorted(((res[i], str(i).zfill(2)) for i in range(40)), reverse=True)[:3]))