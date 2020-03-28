from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
c = sorted(c.items())

if len(c) == 1:
    print(c[0][1])
    exit()

if len(c) == 2:
    if c[1][0] - c[0][0] == 1:
        print(c[0][1]+c[1][1])
    else:
        print(max(c[0][1], c[1][1]))
    exit()

ans = 1
for i in range(1, len(c)-1):
    cnt = c[i][1]
    if c[i+1][0] - c[i][0] == 1:
        cnt += c[i+1][1]
    if c[i][0] - c[i-1][0] == 1:
        cnt += c[i-1][1]
    ans = max(cnt, ans)

print(ans)
