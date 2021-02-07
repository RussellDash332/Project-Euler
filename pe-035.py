from check_primes import is_prime

answer = 1 # 2 is already included
passer = [0,2,4,5,6,8]

for count in range(3,10**6):
    if count < 10 and is_prime(count):
        answer += 1
        continue

    digits = list(map(int,str(count)))
    if False in list(filter(lambda x: x in passer, digits)):
        continue

    flag = True
    n = count
    for _ in range(len(digits)):
        if is_prime(n):
            n = (n//10)+(n%10)*(10**(len(digits)-1))
        else:
            flag = False
            break
    
    if flag:
        answer += 1

print(answer)