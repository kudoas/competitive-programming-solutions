from collections import Counter
from math import factorial

n = int(input())
T = [int(input()) for _ in range(n)]
MOD = 10**9+7
T.sort()
C = Counter(T)
cum_sum = [0]*(n+1)
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + T[i]
cost = sum(cum_sum)

cmb_cnt = 1
for v in C.values():
    cmb_cnt *= factorial(v) % MOD

print(cost)
print(cmb_cnt % MOD)
