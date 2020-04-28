n = int(input())
a = list(map(int, input().split()))

cum_sum = [0] * (n+1)
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + a[i]

INF = 10**18
ans = INF
for i in range(1, n):
    ans = min(ans, abs(cum_sum[i]-(cum_sum[-1]-cum_sum[i])))

print(ans)
