count = 2
answer = 0

n = 5
track = False # Check how far has the program work, currently not set to True

while count < 10**(n+1):
    split = str(count)
    ps = 0
    for i in range(len(split)):
        ps += (int(split[i]))**n
    if ps == count:
        answer += count
    count += 1
    if count % 10**(n-1) == 0 and track:
        print("Reaching "+str(count)+"...")

print(answer)