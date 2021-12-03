from math import log10

n = 0
for i in range(1, 100):
	for j in range(1, 10):
		if i == int(log10(j) * i) + 1:
			n += 1

print(n)