num = []
cyc = []
  
for i in range(2,1000):
    if i % 2 != 0 and i % 5 != 0:
        count = 1
        while (10**count-1) % i != 0:
            count += 1
        print(f"n = {i} cycle = {count}")
        num.append(i)
        cyc.append(count)
    else:
        pass
print()
print(f"n = {num[cyc.index(max(cyc))]} maximum cycle = {cyc[cyc.index(max(cyc))]}")