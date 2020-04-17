from collections import Counter
n = int(input())
d = list(map(int, input().split()))

if d[0] != 0:
    print(0)
    exit()

cnt = Counter(d)

if cnt[0] != 1:
    print(0)
    exit()

ans = 1
for i in d:
    if i != 0:
        ans = (ans * cnt[i-1]) % 998244353
print(ans)
