# n, m, x = map(int, input().split())
# ca = [tuple(map(int, input().split())) for _ in range(n)]

# INF = 10**18
# ans = INF
# for i in range(2**n):
#     ls = [0]*m
#     money = 0
#     for j in range(n):
#         if (i >> j & 1):
#             for k in range(m):
#                 ls[k] += ca[j][k+1]
#             money += ca[j][0]
#     if min(ls) >= x:
#         ans = min(ans, money)

# print(-1 if ans == INF else ans)

from itertools import product
n, m, x = map(int, input().split())
ca = [tuple(map(int, input().split())) for _ in range(n)]
INF = 10**18
ans = INF
for i in product([0, 1], repeat=n):
    cost = 0
    smart = [0]*m
    for j in range(n):
        if i[j] == 0:
            continue
        c, *a = ca[j]
        cost += c
        for k in range(m):
            smart[k] += a[k]

    if all(x <= y for y in smart):
        ans = min(ans, cost)

print(ans if ans != INF else -1)
