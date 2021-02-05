def u(n):
    return (2*((n+3)//4)*n)-((2*((n+3)//4))*((2*((n+3)//4))-1)-1)
  
spiral_size = 1001
diag_sum = 0

for i in range(2*spiral_size-1):
    diag_sum += u(i+1)

print(diag_sum)
