n = int(input())
xy = []
for _ in range(n):
    i = int(input())
    ls = []
    for _ in range(i):
        ls.append(list(map(int, input().split())))
    xy.append(ls)

ans = 0
for i in range(2**n):
    _true = [0]*n
    bl = True
    cnt = 0
    for j in range(n):
        if (i >> j) & 1:
            _true[j] = 1
    for j in range(n):
        if _true[j] == 1:
            for x, y in xy[j]:
                if _true[x-1] != y:
                    bl = False
                    break
    if bl:
        cnt = sum(_true)
    ans = max(ans, cnt)

print(ans)
