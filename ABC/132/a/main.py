import itertools
import sys
input = sys.stdin.readline

s = list(input().rstrip('\n'))
s.sort()
gr = itertools.groupby(s)
ks = []
gs = []

for k, g in gr:
    ks.append(k)
    gs.append(len(list(g)))

if len(ks) == 2 and gs.count(2) == 2:
    print('Yes')
else:
    print('No')
