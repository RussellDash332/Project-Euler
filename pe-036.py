from palindromes import is_palindromic

answer = 0
for n in range(1,10**6):
    if is_palindromic(n) and is_palindromic(bin(n)[2:]):
        answer += n

print(answer)