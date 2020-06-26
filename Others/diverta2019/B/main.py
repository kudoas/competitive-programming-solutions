r, g, b, n = map(int, input().split())
ans = 0
for i in range(3001):
    for j in range(3001):
        v = i*r + j*g
        if n >= v and (n-v) % b == 0:
            ans += 1
print(ans)
