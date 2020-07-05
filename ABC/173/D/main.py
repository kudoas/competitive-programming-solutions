from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
_max = A.count(A[0])
d = defaultdict(int)
for a in A:
    d[a] += 1
waku = []
for k, v in d.items():
    if A[0] == k:
        for _ in range(v):
            waku.append(k)
    else:
        for _ in range(v+1):
            waku.append(k)
if d[A[0]] != 1:
    for _ in range(d[A[0]]-1):
        waku.append(A[0])
waku.sort(reverse=True)
ans = 0
for i in range(n-1):
    ans += waku[i]
print(ans)
