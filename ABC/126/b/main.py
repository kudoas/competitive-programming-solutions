s = input()
s = [int(i) for i in s]

if 1 <= s[0]*10+s[1] <= 12:
    if 1 <= s[2]*10+s[3] <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 1 <= s[2]*10+s[3] <= 12:
    if 1 <= s[0]*10+s[1] <= 12:
        print('AMBIGUOUS')
    else:
        print('YYMM')
else:
    print('NA')
