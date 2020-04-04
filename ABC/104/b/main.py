s = list(input())

bl = False
s1 = s[1]
s2 = s[2:len(s)-1]
s3 = s[-1]

if s[0] == 'A' and s[2:len(s)-1].count('C') == 1:
    s2.remove('C')
    s2 = ''.join(s2)
    ss = s1+s2+s3
    if ss.islower():
        bl = True

print('AC' if bl else 'WA')
