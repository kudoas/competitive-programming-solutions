n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
increase = []
for i in range(n-1):
    if A[i] < A[i+1]:
        increase.append(1)
    else:
        increase.append(0)

cum_sum = [0] * (n)
for i in range(n-1):
    cum_sum[i+1] += cum_sum[i] + increase[i]

ans = 0
for i in range(n-k+1):
    if cum_sum[i+k-1] - cum_sum[i] == k-1:
        ans += 1

print(ans)
