n, a, b = map(int, input().split())
X = list(map(int, input().split()))
cost = [0]*n
for i in range(n-1):
    if (X[i+1] - X[i])*a > b:
        cost[i+1] = b
        continue
    cost[i+1] = (X[i+1] - X[i])*a
ans = sum(cost)
print(ans)
