n = int(input())
ls = []

for i in range(n):
    s, p = input().split()
    p = int(p)
    ls.append([s, -p, i+1])

ls.sort()
for l in ls:
    print(l[2])
