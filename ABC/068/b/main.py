n = int(input())
ans = 0
ls = []

for i in range(1, n+1):
    cnt = 0
    while i % 2 == 0:
        i /= 2
        cnt += 1
    ans = max(ans, cnt)
    ls.append(ans)

print(ls.index(max(ls))+1)
