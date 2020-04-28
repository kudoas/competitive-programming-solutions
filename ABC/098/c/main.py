n = int(input())
s = input()
cum_sum = [0]*(n+1)

for i in range(n):
    if s[i] == "E":
        cum_sum[i+1] += 1
    cum_sum[i+1] += cum_sum[i]

INF = 10**18
ans = INF
for i in range(1, n+1):
    ans = min(ans, (((i-1)-cum_sum[i-1])+(cum_sum[n]-cum_sum[i])))

print(ans)
