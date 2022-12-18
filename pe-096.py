sudoku = open('resources/p096_sudoku.txt', 'r').readlines()

def solve(m):
    DIM = len(m)
    SECT = int(DIM**0.5)

    def check(r, c, val):
        for i in range(DIM):
            if m[r][i] == val: return False
            if m[i][c] == val: return False
        rs, cs = r-r%SECT, c-c%SECT
        for i in range(SECT):
            for j in range(SECT):
                if m[rs+i][cs+j] == val: return False
        return True

    def backtrack(r, c):
        if (r, c) == (DIM-1, DIM): return True
        elif c == DIM: return backtrack(r+1, 0)
        elif m[r][c] > 0: return backtrack(r, c+1)
        for i in range(1, DIM+1):
            if check(r, c, i):
                m[r][c] = i
                if backtrack(r, c+1): return m
        m[r][c] = 0
        return False
    return backtrack(0, 0)

ans = 0
for grid in range(len(sudoku) // 10):
    m = []
    for i in range(10*grid+1, 10*(grid+1)):
        m.append(list(map(int, sudoku[i].strip())))
    res = solve(m)
    a, b, c = res[0][:3]
    ans += 100*a+10*b+c
print(ans)