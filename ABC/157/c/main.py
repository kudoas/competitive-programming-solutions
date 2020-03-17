n, m = map(int, input().split())
ss = []
cc = []
num = []

for _ in range(m):
    s, c = map(int, input().split())
    ss.append(s)
    cc.append(c)

for i in range(1000):
    if len(str(i)) != n:
        continue
    cnt = 0
    for s, c in zip(ss, cc):
        if str(i)[s-1] == str(c):
            cnt += 1
    if cnt == len(ss):
        num.append(i)

if num:
    print(num[0])
else:
    print(-1)
