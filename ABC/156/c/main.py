n = int(input())
x = list(map(int, input().split()))
ma = max(x)

ans = 10**9
for j in range(1, ma+1):
    total = 0
    for i in range(n):
        total += (x[i]-j)**2
    ans = min(total, ans)

print(ans)
