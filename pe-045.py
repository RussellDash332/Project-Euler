from sequences import is_triangle, is_hexagonal, is_pentagonal

flag = 0

j = 1
tph = []

while flag != 3:
    i = j*(2*j-1)
    if is_triangle(i) and is_pentagonal(i) and is_hexagonal(i):
        tph.append(i)
        flag += 1
    # print(i) # track
    j += 1

print(tph)
print("Answer:",tph[-1])