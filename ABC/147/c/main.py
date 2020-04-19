n = int(input())
a = []
xy = []

for _ in range(n):
    i = int(input())
    a.append(i)
    ls = []
    for _ in range(i):
        ls.append(list(map(int, input().split())))
    xy.append(ls)

ans = 0
for i in range(2**n):
    # 正直者リスト
    _true = [0]*n
    bl = True
    for j in range(n):
        if (i >> j) & 1:
            _true[j] = 1
    for j in range(n):
        # 正直者の話だけ聞く
        if _true[j] == 1:
            # 証言を１つずつ確認して矛盾があったら終わり
            for x, y in xy[j]:
                if _true[x-1] != y:
                    bl = False
                    break
    if bl:
        ans = max(ans, sum(_true))

print(ans)
