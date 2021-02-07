sol_list = [[],[]]

bound = 1000

for p in range(1,bound+1): # for now, old code uses brute force for the win :-)
    tup = []
    for k in range(1,p//3):
        for m in range(1,p//4+1):
            n = p//(2*m*k)-m
            if m > n and n > 0:
                if k*2*m*(m+n) == p:
                    if [k*(m**2-n**2),k*2*m*n,k*(m**2+n**2)] not in tup and [k*2*m*n,k*(m**2-n**2),k*(m**2+n**2)] not in tup:
                        tup.append([k*(m**2-n**2),k*2*m*n,k*(m**2+n**2)])
                        print([k*(m**2-n**2),k*2*m*n,k*(m**2+n**2)])
    
    sol = len(tup)
    sol_list[0].append(p)
    sol_list[1].append(sol)

print()
print("Answer:",sol_list[0][sol_list[1].index(max(sol_list[1]))])

#(a,b,c)=(m^2-n^2,2mn+m^2+n^2) -> p = 2m(m+n) and m > n