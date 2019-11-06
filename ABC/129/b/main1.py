n = int(input())
W = list(map(int, input().split()))
ans = float('inf')

for i in range(n):
    ans = min(ans, abs(sum(W[:i])-sum(W[i:])))

print(ans)
