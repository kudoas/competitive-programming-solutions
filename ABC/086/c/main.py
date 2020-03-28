n = int(input())

t0, x0, y0 = 0, 0, 0
cnt = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    diff_t = t-t0
    distance = abs(x0-x)+abs(y0-y)
    if diff_t >= distance and (diff_t - distance == 0 or (diff_t - distance) % 2 == 0):
        cnt += 1
    t0, x0, y0 = t, x, y

print('Yes' if cnt == n else 'No')
