import requests

pell = {}
r = requests.get('https://oeis.org/A002350/b002350.txt')
for line in r.content.decode().strip().split('\n')[1:]:
    D, x = map(int, line.split())
    if D <= 1000: pell[D] = x
print(max(pell, key=pell.get))