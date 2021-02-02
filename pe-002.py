n1 = 1
n2 = 2
even = 2
while n2 < 4000000:
    x = n1+n2
    if x > 4000000:
        break
    n1,n2 = n2,x
    if x % 2 == 0:
        even += x
print(even)