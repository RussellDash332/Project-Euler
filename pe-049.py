from check_primes import is_prime
from itertools import permutations 

def lex(s): 
    perm = sorted(''.join(chars) for chars in permutations(s))
    lp = set() 

    for i in range(len(perm)):
        if int(perm[i]) >= 1000:
            lp.add(int(perm[i]))
    
    a = list(lp)
    a.sort()

    return a

num = [0,1,2,3,4,5,6,7,8,9]
nnz = [1,2,3,4,5,6,7,8,9]

def do():
    for a in range(len(nnz)):
        for b in range(len(num)):
            for c in range(len(num)):
                for d in range(len(num)):
                    s = str(nnz[a])+str(num[b])+str(num[c])+str(num[d])
                    if len(lex(s)) > 2:
                        for i in range(len(lex(s))):
                            for k in range(i+2,len(lex(s))):
                                for j in range(i+1,k):
                                    if is_prime(lex(s)[i]) and is_prime(lex(s)[j]) and is_prime(lex(s)[k]) and lex(s)[i]+lex(s)[k] == 2*lex(s)[j]:
                                        print(lex(s)[i],lex(s)[j],lex(s)[k])
                                        if 1487 not in [lex(s)[i],lex(s)[j],lex(s)[k]]:
                                            print("Answer: "+"".join([str(lex(s)[i]),str(lex(s)[j]),str(lex(s)[k])]))
                                            return
                    print(s) # track
do()