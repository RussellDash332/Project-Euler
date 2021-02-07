import itertools

perm = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

identity = set()
for i in range(len(perm)):
    left = int(str(perm[i][0])+str(perm[i][1]))
    right = int(str(perm[i][2])+str(perm[i][3])+str(perm[i][4]))
    result = int(str(perm[i][5])+str(perm[i][6])+str(perm[i][7])+str(perm[i][8]))
    if left*right == result:
        identity.add(result)
        print('%d x %d = %d'%(left,right,result))

for i in range(len(perm)):
    left = int(str(perm[i][0]))
    right = int(str(perm[i][1])+str(perm[i][2])+str(perm[i][3])+str(perm[i][4]))
    result = int(str(perm[i][5])+str(perm[i][6])+str(perm[i][7])+str(perm[i][8]))
    if left*right == result:
        identity.add(result)
        print('%d x %d = %d'%(left,right,result))
        
print()
print(identity)
print(sum(identity))