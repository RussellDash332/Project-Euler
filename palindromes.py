def is_palindromic(n): # Takes string/integer, checks whether the int version is palindromic
    return int(n)==int(str(n)[::-1])