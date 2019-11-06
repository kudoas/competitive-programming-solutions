import itertools
import sys
input = sys.stdin.readline

s = list(input().rstrip('\n'))
gr = itertools.groupby(s)
ans = 0
keys = []
ls = []

for key, group in gr:
    l = len(list(group))
    keys.append(key)
    ls.append(l)
    for i in range(1, l+1):
        ans += i

for i in range(len(ls)-1):
    if s[0] == '<' and i % 2 == 0 and ls[i] > ls[i+1] and i+1 != len(ls)-1:
        ans -= ls[i+1]
    elif s[0] == '>' and i % 2 == 1 and ls[i] > ls[i+1] and i+1 != len(ls)-1:
        ans -= ls[i+1]

if keys[0] == '<' and ls[0] == 1:
    ans -= 1
if keys[-1] == '>' and ls[-1] == 1:
    ans -= 1

print(ans)
