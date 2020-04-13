# pypy
from collections import Counter

n = int(input())
s = input()
c = Counter(s)
cnt = c['R'] * c['G'] * c['B']

for i in range(n-2):
    for j in range(i+1, n-1):
        w = j - i
        if j+w >= n:
            continue
        if s[i] != s[j] and s[j+w] != s[j] and s[j+w] != s[i]:
            cnt -= 1

print(cnt)
