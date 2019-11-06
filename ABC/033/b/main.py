n = int(input())
m = 0
s = []
p = []

for i in range(n):
    l = list(input().split())
    s.append(l[0])
    p.append(int(l[1]))
    m += int(l[1])

if max(p) > m/2:
    print(s[p.index(max(p))])
else:
    print('atcoder')
