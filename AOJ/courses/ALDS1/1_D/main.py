# n = int(input())
# R = [int(input()) for _ in range(n)]
# INF = 10**18
# ans = -INF
# TLE
# for i in range(n-1):
#     for j in range(i+1, n):
#         ans = max(ans, R[j]-R[i])
# print(ans)

n = int(input())
R = [int(input()) for _ in range(n)]
INF = 10**18
ans = -INF
minv = R[0]
for i in range(1, n):
    ans = max(ans, R[i]-minv)
    minv = min(minv, R[i])
print(ans)
