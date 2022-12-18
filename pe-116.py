def f(k):
    def h(n):
        a = [1]*k
        for _ in range(n-k+1):
            a.append(a[-1] + a[-k])
            a.pop(0)
        return a[-1] - 1
    return h

def t(n):
    r, g, h = f(2), f(3), f(4)
    return r(n) + g(n) + h(n)

print(t(50))