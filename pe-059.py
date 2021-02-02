text = list(map(int,open("resources/p059_cipher.txt","r").readline().split(",")))

# 97-122 for a-z
##for i in range(97,123):
##    for j in range(97,123):
##        for k in range(97,123):
##            key = [i,j,k]
##            text2 = [chr(text[m]^key[m%3]) for m in range(len(text))]
##            result = ''.join(text2)
##            print(key)
##            #print(result)
##            if set(map(ord,result)).issubset(set([i for i in range(32,127)])
##                                             ):
##                print('DONE')
##                print(result)
##                a = input()
##                #raise Exception('Done')
##            #a = input()

# The commented code above is the brute force process to find the right key as below.
key = [101,120,112]
final = [chr(text[m]^key[m%3]) for m in range(len(text))]
asc = list(map(ord,final))
result = ''.join(final)
print(result)
print("\n%d"%(sum(asc)))