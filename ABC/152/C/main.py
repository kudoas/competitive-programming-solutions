n = int(input())
P = list(map(int, input().split()))

ans = 0
INF = 10**18
m = INF
for p in P:
    if p <= m:
        ans += 1
    m = min(m, p)

print(ans)
