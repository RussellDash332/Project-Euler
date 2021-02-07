from check_primes import is_prime

num = 11
count = 0
answer = 0

while count < 11:
    flag = True
    n1 = num
    n2 = num

    # truncatable from right to left
    for _ in range(len(str(num))):
        if is_prime(n1):
            n1 //= 10
        else:
            flag = False
            break

    # truncatable from left to right
    if flag:
        for i in range(len(str(num))):
            if is_prime(n2):
                n2 %= 10**(len(str(num))-i-1)
            else:
                flag = False
                break
        if flag:
            answer += num
            count += 1
            print(num)

    num += 2 # odd numbers only

print("Answer:",answer)