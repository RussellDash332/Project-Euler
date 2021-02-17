from check_sequences import *
from itertools import permutations

# Intuitive, but too long
"""
for i in range(1000,10000): # n1 = i
    if i % 100 > 9 and is_octagonal(i):
        print(i)
        for j in range(10,100):
            n2 = (i % 100) * 100 + j
            for k in range(10,100):
                n3 = (n2 % 100) * 100 + k
                for l in range(10,100):
                    n4 = (n3 % 100) * 100 + l
                    for m in range(10,100):
                        n5 = (n4 % 100) * 100 + m
                        n6 = (n5 % 100) * 100 + (i // 100)
                        check = [i,n2,n3,n4,n5,n6]
                        if len(set(check)) == 6:
                            # print(check) # tracker
                            properties = [is_triangle,is_square,is_pentagonal,is_hexagonal,is_heptagonal]
                            satisfied = []
                            for el in check[1:]:
                                for f in properties:
                                    if f(el) and f not in satisfied:
                                        satisfied.append(f)
                                        break
                            if len(satisfied) == 5:
                                print(check)
"""
def is_cyclic(lst):
    for i in range(len(lst)):
        if lst[i] // 100 != lst[i-1] % 100:
            return False
    return True

def main():
    l1 = list(filter(is_triangle,range(1000,10000)))
    l2 = list(filter(is_square,range(1000,10000)))
    l3 = list(filter(is_pentagonal,range(1000,10000)))
    l4 = list(filter(is_hexagonal,range(1000,10000)))
    l5 = list(filter(is_heptagonal,range(1000,10000)))
    l6 = list(filter(is_octagonal,range(1000,10000)))

    check = [l1,l2,l3,l4,l5,l6]
    for a,b,c,d,e,f in permutations(check):
        for e1 in a:
            for e2 in list(filter(lambda x:x // 100 == e1 % 100,b)):
                for e3 in list(filter(lambda x:x // 100 == e2 % 100,c)):
                    for e4 in list(filter(lambda x:x // 100 == e3 % 100,d)):
                        for e5 in list(filter(lambda x:x // 100 == e4 % 100,e)):
                            for e6 in list(filter(lambda x:x // 100 == e5 % 100,f)):
                                if is_cyclic([e1,e2,e3,e4,e5,e6]):
                                    print(e1, e2, e3, e4, e5, e6)
                                    print("Answer:",sum([e1,e2,e3,e4,e5,e6]))
                                    return

main()