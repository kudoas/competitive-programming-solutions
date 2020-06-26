from collections import Counter

n = int(input())
S = [input() for _ in range(n)]
C = Counter(S[0])
for i in range(1, n):
    c = Counter(S[i])
    for k, v in C.items():
        if C[k] > c[k]:
            C[k] = c[k]
C = sorted(C.most_common())
ans = ''
for c in C:
    ans += c[0]*c[1]
print(ans)
