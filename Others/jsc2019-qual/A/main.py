M, D = map(int, input().split())
ans = 0
for m in range(1, M+1):
    for d in range(10, D+1):
        d = str(d)
        d10, d1 = map(int, (d[1], d[0]))
        if d10 >= 2 and d1 >= 2 and d10*d1 == m:
            ans += 1
print(ans)
