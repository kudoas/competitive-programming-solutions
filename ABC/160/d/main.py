from collections import defaultdict

n, x, y = map(int, input().split())
x -= 1
y -= 1

d = defaultdict(int)
for i in range(n-1):
    for j in range(i+1, n):
        path = min([j-i, abs(x-i)+abs(y-j)+1, abs(x-j)+abs(y-i)+1])
        d[path] += 1

for i in range(1, n):
    print(d[i])
