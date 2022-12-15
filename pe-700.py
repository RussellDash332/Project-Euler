from number_theory import congruence

A, B = 1504170715041707, 4503599627370517
INV = congruence(A, 1, B)

C = A
EC = [A]
while len(EC) != 16:
    C += A
    C %= B
    if C <= EC[-1]:
        EC.append(C)

T = EC[-1]
U = 1
EC2 = [U]
while EC2[-1] < T:
    U += 1
    V = U*INV % B
    if EC2[-1]*INV % B > V:
        EC2.append(U)
#print(sorted(set(EC) | set(EC2))[::-1])
print(sum(set(EC) | set(EC2)))