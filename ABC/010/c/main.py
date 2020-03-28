x0, y0, x1, y1, t, v = map(int, input().split())
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    distance = ((x-x0)**2+(y-y0)**2)**0.5 + ((x1-x)**2+(y1-y)**2)**0.5
    max_distance = t*v
    if distance <= max_distance:
        print('YES')
        exit()

print('NO')
