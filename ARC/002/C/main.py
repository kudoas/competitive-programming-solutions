from itertools import permutations

n = int(input())
C = input()
shortcuts = ['AA', 'BB', 'XX', 'YY',
             'AB', 'BA', 'AX', 'XA', 'AY',
             'YA', 'BX', 'XB', 'BY', 'YB', 'XY', 'YX'
             ]
INF = 10**18
ans = -INF
for l, r in permutations(shortcuts, 2):
    cnt = C.count(l)
    cnt += C.replace(l, 'L').count(r)
    if ans < cnt:
        ans = cnt
else:
    ans += n-ans*2
print(ans)
