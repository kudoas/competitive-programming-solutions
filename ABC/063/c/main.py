n = int(input())
ls = []

for _ in range(n):
    s = int(input())
    ls.append(s)

ans = sum(ls)

if ans % 10 == 0:
    ls.sort()
    for i in range(n):
        if ls[i] % 10 != 0:
            ans -= ls[i]
            print(ans)
            exit()
    print(0)
    exit()
else:
    print(ans)
