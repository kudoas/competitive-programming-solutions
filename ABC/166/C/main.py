n, m = map(int, input().split())
h = list(map(int, input().split()))

se = set()
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] <= h[b]:
        se.add(a)
    if h[a] >= h[b]:
        se.add(b)

ans = n - len(se)
print(ans)
