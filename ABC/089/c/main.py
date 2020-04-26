from collections import defaultdict
from itertools import combinations

n = int(input())
d = defaultdict(int)

for _ in range(n):
    s = input()
    if s[0] == 'M':
        d['M'] += 1
    if s[0] == 'A':
        d['A'] += 1
    if s[0] == 'R':
        d['R'] += 1
    if s[0] == 'C':
        d['C'] += 1
    if s[0] == 'H':
        d['H'] += 1

ls = [dd for dd in d]

if len(ls) < 3:
    print(0)
    exit()

ans = 0
for v in combinations(ls, 3):
    cnt = 1
    for vv in v:
        cnt *= d[vv]
    ans += cnt

print(ans)
