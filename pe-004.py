from palindromes import is_palindromic

answer = 0

for a in range(100,1000):
    for b in range(a,1000):
        if is_palindromic(a*b) and a*b > answer:
            answer = a*b
            print(answer)