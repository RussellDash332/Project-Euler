number = "".join(list(map(lambda x:x.strip(),open("resources/p008_number.txt").readlines())))
number_list = [i for i in str(number)]

aj_term = 13
aj_list = []

for i in range(len(number_list)-aj_term+1):
    adjacent = 1
    for j in range(aj_term):
        adjacent *= int(number_list[i+j])
    aj_list.append(adjacent)

print(max(aj_list))