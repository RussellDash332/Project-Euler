def sol(a,b):
    return a*(a+1)*b*(b+1)//4

def do():
    target = 2*10**6
    while True:
        for i in range(1,5001):
            for j in range(i,5001):
                if sol(i,j) == target:
                    print(i*j)
                    return
        target -= 1

do()