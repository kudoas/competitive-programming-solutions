s = input()

n = len(s)
ss1 = s[:int((n-1)/2)]
ss = s[int((n+3)/2)-1:]

if s != s[::-1]:
    print('No')
    exit()
if s[:int((n-1)/2)] != ss1[::-1]:
    print('No')
    exit()
if s[int((n+3)/2)-1:] != ss[::-1]:
    print('No')
    exit()

print('Yes')
