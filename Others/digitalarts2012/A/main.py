S = list(input().split())
n = int(input())
filter = [input() for s in range(n)]
ans = S[:]
p = 0
for s in S:
    p += 1
    l = len(s)
    for f in filter:
        if l != len(f):
            continue
        for i in range(l):
            if f[i] == "*":
                continue
            if s[i] != f[i]:
                break
        else:
            ans[p-1] = "*"*l
print(*ans)
