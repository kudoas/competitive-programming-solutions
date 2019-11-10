from collections import defaultdict
d = defaultdict(int)

n = int(input())
for _ in range(n):
    d[input()] += 1

m = int(input())
for _ in range(m):
    d[input()] -= 1


ans = max(0, max(d.values()))
print(ans)
