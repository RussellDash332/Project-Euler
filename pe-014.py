## Idea from CS1010S

lut = {}

def f(n):
    return 3*n+1 if n%2 else n//2
    
def collatz_terms_memo(n):
    if n == 1:
        return 1
    else:
        if n in lut:
            return lut[n]
        lut[n] = collatz_terms_memo(f(n))+1
        return lut[n]
    
ans = list(map(collatz_terms_memo,range(1,10**6)))
print(ans.index(max(ans))+1)