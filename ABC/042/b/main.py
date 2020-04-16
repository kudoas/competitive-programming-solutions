n, l = map(int, input().split())
ls = sorted([input() for _ in range(n)])
print(*ls, sep='')
