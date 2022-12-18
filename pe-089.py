romans = open('resources/p089_roman.txt', 'r').readlines()

def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    i = 0
    num = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            num += roman[s[i]]
            i +=1
    return num

def intToRoman(num):
    m = ["", "M", "MM", "MMM", "MMMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    ans = (thousands + hundreds + tens + ones)
    return ans

old, new = 0, 0
for roman in romans:
    roman = roman.strip()
    rti = romanToInt(roman)
    itr = intToRoman(rti)
    old += len(roman)
    new += len(itr)
    print(roman, rti, itr)
print(old - new)