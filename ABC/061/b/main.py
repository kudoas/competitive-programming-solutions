n, m = map(int, input().split())
ls = []

for _ in range(m):
    a, b = map(int, input().split())
    ls.append(a)
    ls.append(b)

for i in range(1, n+1):
    print(ls.count(i))
