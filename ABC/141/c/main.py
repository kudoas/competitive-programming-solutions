from collections import Counter

n, k, q = map(int, input().split())
A = [int(input()) for _ in range(q)]
C = Counter(A)
for i in range(1, n+1):
    if C[i] + k - q <= 0:
        print('No')
    else:
        print('Yes')
