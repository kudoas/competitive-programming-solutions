# from itertools import combinations_with_replacement
# from collections import Counter

# TLE
# n, m = map(int, input().split())
# ls = [2, 3, 4]
# for i in combinations_with_replacement(ls, n):
#     if sum(i) == m:
#         c = Counter(i)
#         print(c[2], c[3], c[4])
#         break
# else:
#     print(-1, -1, -1)

# turukame-zan
# n, m = map(int, input().split())
# for b in range(n+1):
#     a = 2*n - (m/2) - (b/2)
#     c = n - a - b
#     if a >= 0 and c >= 0 and a.is_integer() and c.is_integer():
#         print(int(a), int(b), int(c))
#         break
# else:
#     print(-1, -1, -1)

n, m = map(int, input().split())
for c in range(n + 1):
    b = m - 2 * n - 2 * c
    a = n - b - c
    if b >= 0 and a >= 0:
        print(a, b, c)
        break
else:
    print(-1, -1, -1)
