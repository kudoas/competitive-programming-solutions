s = list(input())

if s[0] == 'A' and s[2:].count('C') == 1:
    s.remove('A')
    s.remove('C')
    for ss in s:
        if ss.isupper():
            print('WA')
            exit()
    print('AC')

else:
    print('WA')
