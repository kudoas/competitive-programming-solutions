from collections import defaultdict

n, m = map(int, input().split())

aa = []
bb = []
cc = []
dd = []
answer = []

for i in range(n):
    a, b = map(int, input().split())
    aa.append(a)
    bb.append(b)

for i in range(m):
    c, d = map(int, input().split())
    cc.append(c)
    dd.append(d)

for i in range(n):
    ans = float('inf')
    for j in range(m):
        distance = abs(aa[i]-cc[j]) + abs(bb[i]-dd[j])
        if ans > distance:
            ans = min(distance, ans)
            num = j+1
    answer.append(num)

print(*answer, sep='\n')
