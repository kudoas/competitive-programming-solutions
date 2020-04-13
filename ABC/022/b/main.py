from collections import Counter

n = int(input())
A = [int(input()) for _ in range(n)]
c = Counter(A)

ans = sum(c.values()) - len(c)
print(ans)
