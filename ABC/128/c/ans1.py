n, m = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    for j in range(m):
        cnt = 0
        for k in range(n):
            if (i >> k) & 1 and k+1 in s[j]:
                cnt += 1
        if cnt % 2 != p[j]:
            break
    else:
        ans += 1
print(ans)
