s = open('resources/p107_network.txt', 'r').readlines()
el = []
for i, line in enumerate(s):
    line = line.strip().split(',')
    for j in range(i+1, len(line)):
        if line[j] != '-':
            el.append((int(line[j]), i, j))
el.sort(reverse=True)

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

uf = UFDS(len(s))
msts = sum(map(lambda x: x[0], el))
while el:
    w, i, j = el.pop()
    if not uf.is_same_set(i, j):
        uf.union(i, j)
        msts -= w
print(msts)