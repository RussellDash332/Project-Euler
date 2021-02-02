from check_primes import is_prime
import math

f = list(filter(is_prime,range(3,10000))) # 10000 is sufficient

def concat_prime(n1,n2):
    concat1 = n1*10**(math.floor(math.log10(n2))+1)+n2
    concat2 = n2*10**(math.floor(math.log10(n1))+1)+n1
    return is_prime(concat1) and is_prime(concat2)

result = []
track = False

for a in range(len(f)):
    for b in range(a+1,len(f)):
        if concat_prime(f[a],f[b]):
            for c in range(b+1,len(f)):
                if concat_prime(f[a],f[c]) and concat_prime(f[b],f[c]):
                    for d in range(c+1,len(f)):
                        if concat_prime(f[a],f[d]) and concat_prime(f[b],f[d]) and concat_prime(f[c],f[d]):
                            for e in range(d+1,len(f)):
                                if concat_prime(f[a],f[e]) and concat_prime(f[b],f[e]) and concat_prime(f[c],f[e]) and concat_prime(f[d],f[e]):
                                    ps = [f[a],f[b],f[c],f[d],f[e]]
                                    if not track:
                                        print(ps,sum(ps))
                                    result.append([ps,sum(ps)])
                                elif track:
                                    print([f[a],f[b],f[c],f[d],f[e]])
                        elif track:
                            print([f[a],f[b],f[c],f[d]])
                elif track:
                    print([f[a],f[b],f[c]])
        elif track:
            print([f[a],f[b]])
print('DONE')
for r in result:
    print(r[0],r[1])