from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
q = int(input())
BC = [tuple(map(int, input().split())) for _ in range(q)]
total = sum(A)
d = defaultdict(int)
for a in A:
    d[a] += 1
for b, c in BC:
    total = total - b*d[b] + c*d[b]
    d[c] += d[b]
    d[b] = 0
    print(total)
