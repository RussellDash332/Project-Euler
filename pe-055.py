from palindromes import is_palindromic

def reverse(n):
    return int(str(n)[::-1])

non_lychrel = 0
bound = 10000

# finds the number of non-lychrel numbers from 1 to bound, meaning these numbers will become a palindrome in < 50 iterations.
for i in range(1,bound):
    is_lychrel = True
    n = i
    for j in range(55):
        if is_palindromic(n) and n!= i:
            non_lychrel += 1
            #print(i,j)
            is_lychrel = False
            break
        n += reverse(n)
    if is_lychrel:
        print(i, end = " ")
print()
print("Lychrel numbers :",bound-1-non_lychrel)
