def f(k):
    def h(n):
        a = [0]*(k-1) + [1]
        for _ in range(n):
            a.append(sum(a))
            a.pop(0)
        return a[-1]
    return h

print(f(4)(50))