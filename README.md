# Project Euler
Basically all my [Project Euler](https://projecteuler.net/) relevant codes, mainly in Python.
> You can also do Project Euler+ by HackerRank [here](https://www.hackerrank.com/contests/projecteuler/challenges).
I have put all the current necessary resources on the ["resources"](https://github.com/RussellDash332/Project-Euler/tree/main/resources) folder.

#### Some functions where you can import from
+ [check_primes](https://github.com/RussellDash332/Project-Euler/blob/main/check_primes.py)
    + ```is_prime```, checks whether a positive integer is a prime number
    + ```is_composite```, the exact opposite of ```is_prime```
    + ```sieve```, returns a list of all prime numbers up to the input integer
+ [check_sequences](https://github.com/RussellDash332/Project-Euler/blob/main/check_sequences.py)
    + ```is_triangle```, checks whether an integer is in the form ```n(n+1)/2```
    + ```is_pentagonal```, checks whether an integer is in the form ```n(3n-1)/2```
    + ```is_hexagonal```, checks whether an integer is in the form ```n(2n-1)```
+ [choose](https://github.com/RussellDash332/Project-Euler/blob/main/choose.py)
    + ```binom```, takes two integers ```n``` and ```r```, returning ```nCr```
+ [number_theory](https://github.com/RussellDash332/Project-Euler/blob/main/number_theory.py)
    + ```gcd```, takes two integer inputs and returns the GCD of both integers
    + ```lcm```, takes two integer inputs and returns the LCM of both integers
    + ```factorial```, returns the factorial of the integer input
    + ```factor```, returns the number of positive factors of the input integer
    + ```sum_factor```, returns the sum of all positive factors of the input integer
    + ```fib```, returns the n-th Fibonacci number, where n is the input
+ [palindromes](https://github.com/RussellDash332/Project-Euler/blob/main/palindromes.py)
    + ```is_palindromic```, checks whether an *integer* or *string-ized integer* is a palindrome

#### Noob Notes 🤪
Some problems are solved using sequences (lists, tuples, dictionaries, etc) which is computationally more expensive compared to assigning and modifying a constant number of variables. This is because it was done a very long time ago. For now, I've only decided to improve some, especially the first problems. Maybe more in the future.