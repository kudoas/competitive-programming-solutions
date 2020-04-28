import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cum_sum = [0]*n

total = 0
for i in range(n):
    total += a[i]
    cum_sum[i] = total

max_sum = cum_sum[-1]

ans = abs(cum_sum[0]-(max_sum-cum_sum[0]))
for i in range(n-1):
    ans = min(ans, abs(cum_sum[i]-(max_sum-cum_sum[i])))

print(ans)
