n = int(input())
a = list(map(int, input().split()))
s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]
INF = 10**18
ans = INF
for R in range(1, n):
    ans = min(ans, abs((s[R]-s[0])-(s[n]-s[R])))
print(ans)
