n, m = map(int, input().split())
ab = []

for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

ab.sort()
answer = 0

for a, b in ab:
    buy = min(m, b)
    m -= buy
    ans += a*buy

print(ans)
