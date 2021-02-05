n = list(map(lambda x:list(map(int,x.strip().split(" "))),open("resources/p011_number.txt").readlines()))

max_adj = 0

for i in range(len(n)-3):
    for j in range(len(n[0])-3):
        hori = n[i][j]*n[i][j+1]*n[i][j+2]*n[i][j+3]
        verti = n[i][j]*n[i+1][j]*n[i+2][j]*n[i+3][j]
        diag_down = n[i][j]*n[i+1][j+1]*n[i+2][j+2]*n[i+3][j+3]
        diag_up = n[i][j+3]*n[i+1][j+2]*n[i+2][j+1]*n[i+3][j]

        if hori > max_adj:
            max_adj = hori
        if verti > max_adj:
            max_adj = verti
        if diag_down > max_adj:
            max_adj = diag_down
        if diag_up > max_adj:
            max_adj = diag_up
  
print(max_adj)