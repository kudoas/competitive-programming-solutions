n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for x, y in ls:
    for _x, _y in ls:
        if (x, y) == (_x, _y):
            continue
        l = ((_x-x)**2+(_y-y)**2)**0.5
        ans = max(ans, l)

print(ans)
