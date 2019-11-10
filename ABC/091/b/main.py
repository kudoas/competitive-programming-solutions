n = int(input())
ss = [input() for _ in range(n)]
m = int(input())
tt = [input() for _ in range(m)]
ans = 0

for s in ss:
    ans = max(ans, (ss.count(s)-tt.count(s)))

print(ans)
