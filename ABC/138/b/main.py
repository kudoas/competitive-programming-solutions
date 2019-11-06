n = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(n):
    ans += 1/A[i]

print(1/ans)
