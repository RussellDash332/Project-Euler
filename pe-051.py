from check_primes import is_prime

def check(initial):
    div = list(str(initial))
    zero = 0
    for i in range(len(div)):
        if div[i] == '0':
            zero += 10**(len(div)-i-1)
    zero2 = 10**len(div)+zero
    lst1 = [initial+zero*i for i in range(10)]
    lst2 = [initial+zero2*i for i in range(1,10)]
    numbers1 = list(filter(is_prime,lst1))
    numbers2 = list(filter(is_prime,lst2))
    print(numbers1)
    print(numbers2)
    return [initial, len(numbers1),len(numbers2)]

for i in range(1,1000001,2):
    a = check(i)
    print(a[0])
    
    if a[1] == 8 or a[2] == 8:
        print('FOUND!')
        break