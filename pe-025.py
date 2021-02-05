from number_theory import fib
import math


n = 1
while math.log(fib(n),10) < 999:
    n += 1
print(n)