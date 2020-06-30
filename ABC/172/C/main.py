import bisect

n, m, k = map(int, input().split())
INF = 10**18
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cum_a = [0] * (n+1)
cum_b = [0] * (m+1)
for i in range(n):
    cum_a[i+1] = cum_a[i] + A[i]
for i in range(m):
    cum_b[i+1] = cum_b[i] + B[i]
INF = 10**18
ans = -INF
for i in range(n+1):
    mod = k - cum_a[i]
    b = bisect.bisect(cum_b, mod)
    if b == 0:
        ans = max(ans, i)
        break
    ans = max(ans, b+i)
ans -= 1
print(ans)
