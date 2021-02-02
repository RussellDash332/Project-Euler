m = 1
for i in range(1,501):
    # n = round((500/m)-m) ## <- m(m+n)=500 (actually inaccurate due to floating point)
    n = 1
    while m*(m+n) != 500:
        n += 1
        if m*(m+n) > 500:
            break
    if m*(m+n) == 500 and m>n>0:
        if (m**2-n**2<2*m*n<m**2+n**2) or (m**2+n**2>m**2-n**2>2*m*n):
            #print(m,n)
            print('a = %d, b = %d, c = %d'%(m**2-n**2,2*m*n,m**2+n**2))
            print('abc = %d'%((m**2-n**2)*2*m*n*(m**2+n**2)))
            print()
    m += 1