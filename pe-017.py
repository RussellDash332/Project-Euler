to_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundred = 7
thousand = 8
total = 0
for i in range(1,1000):
    u = i%10
    t = int(((i%100)-u) /10)
    h = int(((i%1000)-(t*10)-u) /100)
    #print(h,t,u)

    if i < 20:                                                          # the number is less than 20
        total += to_19[i]
    elif h != 0 and (t != 0 or u != 0):                                 # the number is over 100 but not a multiple of 100
        if t == 0 or t == 1:                                            # the number is between x01 and x19
            total += to_19[h] + hundred + 3 + to_19[(t * 10) + u]
        else:                                                           # the number is between x20 and x99
            total += to_19[h] + hundred + 3 + tens[t] + to_19[u]
    elif t == 0 and u == 0:                                             # the number is a multiple of 100
        total += to_19[h] + hundred
    else:                                                               # the number is between 20 and 99
        total +=  tens[t] + to_19[u]

print(total+thousand+3) # 3 from "one" at "one thousand"