from z3 import *

models = []
a, b, c, d, e, f, g, h, i, j = [Int(z) for z in 'abcdefghij']

def sol(x):
    bef = len(models)
    s = Solver()
    for args in [
        a + b + c == x,
        d + c + e == x,
        f + e + g == x,
        h + g + i == x,
        j + i + b == x,
        a > 0, a < 11,
        b > 0, b < 11,
        c > 0, c < 11,
        d > 0, d < 11,
        e > 0, e < 11,
        f > 0, f < 11,
        g > 0, g < 11,
        h > 0, h < 11,
        i > 0, i < 11,
        j > 0, j < 11,
        a != b, a != c, a != d, a != e, a != f, a != g, a != h, a != i, a != j,
        b != c, b != d, b != e, b != f, b != g, b != h, b != i, b != j,
        c != d, c != e, c != f, c != g, c != h, c != i, c != j,
        d != e, d != f, d != g, d != h, d != i, d != j,
        e != f, e != g, e != h, e != i, e != j,
        f != g, f != h, f != i, f != j,
        g != h, g != i, g != j,
        h != i, h != j,
        i != j
    ]:
        s.add(args)

    while s.check() == sat:
        m = s.model()
        models.append(m)
        s.add(
            Or(
                a != m[a],
                Or(
                    b != m[b],
                    Or(
                        c != m[c],
                        Or(
                            d != m[d],
                            Or(
                                e != m[e],
                                Or(
                                    f != m[f],
                                    Or(
                                        g != m[g],
                                        Or(
                                            h != m[h],
                                            Or(
                                                i != m[i],
                                                j != m[j]
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    return len(models) - bef


for x in range(14, 20):
    sol(x)

'''
a, b, c; d, c, e; f, e, g; h, g, i; j, i, b
'''

len16 = []
for solu in models:
    s = [
        [int(solu[a].as_string()), int(solu[b].as_string()), int(solu[c].as_string())],
        [int(solu[d].as_string()), int(solu[c].as_string()), int(solu[e].as_string())],
        [int(solu[f].as_string()), int(solu[e].as_string()), int(solu[g].as_string())],
        [int(solu[h].as_string()), int(solu[g].as_string()), int(solu[i].as_string())],
        [int(solu[j].as_string()), int(solu[i].as_string()), int(solu[b].as_string())]
    ]
    idx = s.index(min(s))
    s2 = s[idx:] + s[:idx]
    s3 = ''.join(map(lambda x: ''.join(map(str, x)), s2))
    if len(s3) == 16:
        len16.append([s2, s3])
print(max(len16)[1])