n = int(input())
A = list(map(int, input().split()))
INF = 10**18
ans = INF
for i in range(-100, 101):
    cnt = 0
    for a in A:
        cnt += (i-a)**2
    ans = min(ans, cnt)
print(ans)
