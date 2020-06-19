x, n = map(int, input().split())
P = list(map(int, input().split()))
INF = 10**18
ans = INF
for i in range(-100, 102):
    if i in P:
        continue
    if ans > abs(x-i):
        ans = abs(x-i)
        cnt = i
print(cnt)
