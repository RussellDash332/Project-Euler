cards = list(map(lambda x:[x.strip().split(" ")[0:5],x.strip().split(" ")[5:10]],open('resources/p054_poker.txt').readlines()))
count = 0

# Unnecessary but to make it more layman
status = {
    'royal flush': 10,
    'straight flush': 9,
    'four of a kind': 8,
    'full house': 7,
    'flush': 6,
    'straight': 5,
    'three of a kind': 4,
    'two pairs': 3,
    'one pair': 2,
    'high card': 1
    }
ranks = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
}

def is_consecutive(sorted_list):
    for i in range(1,len(sorted_list)):
        if sorted_list[i] != sorted_list[i-1] + 1:
            return False
    return True

def check(p): # reveals the status of p
    sorted_p = sorted(p, key=lambda x:ranks[x[0]])
    suit_dict = {}
    rank_map = list(map(lambda x: ranks[x[0]],sorted_p))
    rank_dict = {}

    for card in p:
        suit_dict[card[1]] = suit_dict.get(card[1],0)+1
        rank_dict[ranks[card[0]]] = rank_dict.get(ranks[card[0]],0)+1

    if rank_map == [10,11,12,13,14] and len(suit_dict) == 1:
        return status['royal flush']                        # no tie needed
    elif is_consecutive(rank_map) and len(suit_dict) == 1:
        return [status['straight flush'], rank_map[-1]]     # status and highest card from the straight
    elif 4 in rank_dict.values():
        for k in rank_dict:
            if rank_dict[k] == 4:
                return [status['four of a kind'], k, list(filter(lambda x: rank_dict[x] == 1,rank_dict.keys()))[0]]
                                                            # status and rank from the 4 of a kind plus the remaining card
    elif 3 in rank_dict.values() and 2 in rank_dict.values():
        for k in rank_dict:
            if rank_dict[k] == 3:
                return [status['full house'], k, list(filter(lambda x: rank_dict[x] == 2,rank_dict.keys()))[0]]
                                                            # status and rank from the fullhouse trio then the duo
    elif len(suit_dict) == 1:
        return [status['flush']] + rank_map[::-1]           # status number then the descending order of ranks
    elif is_consecutive(rank_map):
        return [status['straight']] + rank_map[::-1]        # status number then the descending order of ranks
    elif 3 in rank_dict.values():                           # Must be in the form of A A A B C,
                                                            # if A A A B B or A A A B A that's a higher status
        for k in rank_dict:
            if rank_dict[k] == 3:
                return [status['three of a kind'], k] + list(filter(lambda x: x != k, rank_map[::-1]))
                                                            # status number, the trio then the descending order of ranks
    elif list(rank_dict.values()).count(2) == 2:            # Must be in the form of A A B B C
        for i in range(len(rank_dict)):
            for j in range(len(rank_dict)):
                if i != j and list(rank_dict.keys())[i] > list(rank_dict.keys())[j]:
                    return [status['two pairs'],
                            list(rank_dict.keys())[i],      # higher pair
                            list(rank_dict.keys())[j],      # lower pair
                            list(filter(lambda x:           # the remaining card
                                        x != list(rank_dict.keys())[i] and
                                        x != list(rank_dict.keys())[j],
                                rank_dict.keys()))[0]]
    elif 2 in rank_dict.values():
        for k in rank_dict:
            if rank_dict[k] == 2:
                return [status['one pair'], k] + list(filter(lambda x: x != k, rank_map[::-1]))
                                                            # status number, the pair then the descending order of ranks
    else:
        return [status['high card']] + rank_map[::-1]       # status number then the descending order of ranks

track = True # set to True/False to check/skip the visualization
for hand in cards:
    p1,p2 = hand
    if track:
        print(str(sorted(p1, key=lambda x:ranks[x[0]]))+" VS "+str(sorted(p2, key=lambda x:ranks[x[0]]))+" ---> "+str(check(p1))+" VS "+str(check(p2)))
    if check(p1) > check(p2):
        count += 1
print("Answer:",count)