n = int(input())
V = list(map(int, input().split()))
V.sort()
ans = V[0]

for i in range(n-1):
    ans = (ans+V[i+1])/2

print(ans)
