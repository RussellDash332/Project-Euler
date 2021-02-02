nom1, nom2 = 1, 3
denom1, denom2 = 1, 2

iterations = 1000
count = 0

for i in range(2,iterations+1):
    nom = 2*nom2 + nom1
    denom = 2*denom2 + denom1
    if len(str(nom)) > len(str(denom)):
        count += 1
    nom1, nom2 = nom2, nom
    denom1, denom2 = denom2, denom

print(count)