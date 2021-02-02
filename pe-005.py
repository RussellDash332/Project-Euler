from number_theory import gcd, lcm

lcm_final = 1

for i in range(20):
    lcm_final = lcm(lcm_final,i+1)
    print('%d -> %d'%(i+1,lcm_final))