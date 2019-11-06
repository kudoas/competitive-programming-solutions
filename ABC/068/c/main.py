n, m = map(int, input().split())
ls = [[int(i) for i in input().split()] for _ in range(m)]

se1 = set()
se2 = set()

for a, b in ls:
    if a == 1:
        se1.add(b)
    if b == n:
        se2.add(a)

se = se1 & se2

print('POSSIBLE' if se else 'IMPOSSIBLE')
