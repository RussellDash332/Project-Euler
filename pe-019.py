A = [31,28,31,30,31,30,31,31,30,31,30,31]
sunday =0
gK = 1
for y in range(1901,2001):
    if y % 4 == 0:
        A[1] = 29
    else:
        A[1] = 28
    for m in range(len(A)):
        for d in range(1,A[m]+1):
            if(gK ==6):
                if(d==1):
                    sunday +=1
                gK = 0
            else:
                gK += 1
print(sunday)