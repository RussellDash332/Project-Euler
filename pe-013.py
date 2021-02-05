num = list(map(lambda x:int(x.strip()),open("resources/p013_number.txt").readlines()))

print(str(sum(num))[:10])