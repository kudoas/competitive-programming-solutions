n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort()
total = 0
for a, b in ab:
    total += b
    if k <= total:
        print(a)
        break
