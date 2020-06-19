n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n-k+1):
    if i == 0:
        cnt = sum(A[:k])
        ans += cnt
        continue
    cnt = cnt - A[i-1] + A[i+k-1]
    ans += cnt
print(ans)
