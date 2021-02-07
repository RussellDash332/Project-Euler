from sequences import is_pentagonal

flag = True

j = 1

while flag:
    for k in range(1, j):
        a = j*(3*j-1)//2 # i-th pentagonal number
        b = k*(3*k-1)//2 # j-th pentagonal number
        if is_pentagonal(a+b) and is_pentagonal(a-b):
            print(a-b)
            flag = False
            break
    j += 1