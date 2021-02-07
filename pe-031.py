"""
combi = 0
# 1, 2, 4, 10, 20, 40, 100, 200
for a in range(0,6):
    for b in range(0,7-2*a):
        for c in range(0,9-4*a-2*b):
            for d in range(0,15-10*a-5*b-1*c):
                for e in range(0,25-20*a-10*b-5*c-2*d):
                    for f in range(0,45-40*a-20*b-10*c-4*d-2*e):
                        for g in range(0,105-100*a-50*b-25*c-10*d-5*e-1*c):
                            for h in range(0,205-200*a-100*b-50*c-20*d-10*e-5*f-2*g):
                                if h + 2*g + 5*f + 10*e + 20*d + 50*c + 100*b + 200*a == 200:
                                    combi += 1
                                    # print([a,b,c,d,e,f,g,h])

print(combi)
"""

# Count change, idea : CS1010S
def count_change(a,d):
    table = []
    row = [0]*(d+1)
    for i in range(a+1):
        table.append(row.copy())

    for i in range(1,d+1):
        table[0][i] = 1
    for i in range(1,a+1):
        for j in range(1,d+1):
            if i-coins[j-1] >= 0:
                table[i][j] = table[i-coins[j-1]][j] + table[i][j-1]
            else:
                table[i][j] = table[i][j-1]

    return table[a][d]
coins = [200,100,50,20,10,5,2,1]
print(count_change(200,len(coins)))