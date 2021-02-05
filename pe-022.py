names = open("resources/p022_names.txt").read().replace(","," ").replace("\"","").split(" ")

names.sort()
ns_sum = 0
for i in range(len(names)):
    for j in range(len(names[i])):
        ns_sum += (ord(names[i][j])-64)*(i+1)
print(ns_sum)