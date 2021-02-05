triangle = list(map(lambda x:list(map(int,x.strip().split(" "))),open("resources/p067_triangle.txt").readlines()))

for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
    triangle.pop()

print(triangle[0][0])