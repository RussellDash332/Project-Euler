words = open("resources/p042_words.txt").read().replace(","," ").replace("\"","").split(" ")

ws_list = []

for i in range(len(words)):
    ns = 0
    for j in range(len(words[i])):
        for k in range(26):
            if ord(words[i][j]) == 65+k:
                ns += k+1
    ws_list.append(ns)

triangle_word = []
triangle_number = []

for i in range(100):
    triangle_number.append((i+1)*(i+2)//2)

for i in range(len(ws_list)):
    if ws_list[i] in triangle_number:
        triangle_word.append(words[i])

print(len(triangle_word))