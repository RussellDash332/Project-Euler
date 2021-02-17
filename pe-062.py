def main(n1):
    #print(n1)

    lst = sorted(str(n1**3))
    n2 = n1+1
    while (len(sorted(str(n2**3))) <= len(lst)):
        if sorted(str(n2**3)) == lst:
            n3 = n2+1
            while (len(sorted(str(n3**3))) <= len(lst)):
                if sorted(str(n3**3)) == lst:
                    n4 = n3+1
                    while (len(sorted(str(n4**3))) <= len(lst)):
                        if sorted(str(n4**3)) == lst:
                            n5 = n4+1
                            while (len(sorted(str(n5**3))) <= len(lst)):
                                if sorted(str(n5**3)) == lst:
                                    #print(n1,n2,n3,n4,n5)
                                    return n1**3
                                n5 += 1
                        n4 += 1
                n3 += 1
        n2 += 1
    n1 += 1
    return 0

n = 345
while not main(n):
    n += 1
print("Answer:",main(n))