# bit全探索：全てのスイッチに対してONとOFFを確認する
n, m = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))

cnt = 0
for i in range(2**n):
    for j in range(m):
        switch = 0
        for k in range(n):
            if (i >> k & 1) and k+1 in s[j]:
                switch += 1
        if switch % 2 != p[j]:
            break
    else:
        cnt += 1

print(cnt)
