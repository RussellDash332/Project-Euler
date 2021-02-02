from check_primes import is_prime

def spiral2(n): # assume n is odd
    diag = (n+1)//2
    ne = list(4*(i+1)**2-10*(i+1)+7 for i in range(1,diag))
    es = list(4*(i+1)**2-4*(i+1)+1 for i in range(1,diag))
    ws = list(4*(i+1)**2-6*(i+1)+3 for i in range(1,diag))
    nw = list(4*(i+1)**2-8*(i+1)+5 for i in range(1,diag))
    result = [1]+ne+es+ws+nw
    return len(list(filter(is_prime,result)))/len(result)*100

##i = 5
##while spiral2(i) >= 10:
##    i += 2
##    print(i)
##print('DONE',i)

prime = 8
numbers = 13
spiral = 7
while prime/numbers >= 0.1:
    #print(spiral)
    diag = (spiral+1)//2
    if is_prime(4*(diag+1)**2-10*(diag+1)+7):
        prime += 1
    if is_prime(4*(diag+1)**2-8*(diag+1)+5):
        prime += 1
    if is_prime(4*(diag+1)**2-6*(diag+1)+3):
        prime += 1
    if is_prime(4*(diag+1)**2-4*(diag+1)+1):
        prime += 1
    numbers += 4
    spiral += 2
print('DONE',spiral)
