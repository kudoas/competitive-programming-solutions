n, m = map(int, input().split())
se = set()
start = set()
start.add(1)
for i in range(m):
    x, y = map(int, input().split())
    if x in start:
        start.add(y)
        se.add(y)
print(len(se))
