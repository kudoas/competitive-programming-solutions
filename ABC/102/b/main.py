import itertools

n = int(input())
A = list(map(int, input().split()))
ans = -float('inf')
cn = itertools.combinations(A, 2)

for a, b in cn:
    cnt = abs(a-b)
    ans = max(ans, cnt)

print(ans)
