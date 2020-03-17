from collections import defaultdict

n = int(input())
d = defaultdict(int)
cnt = 0

for _ in range(n):
    d[int(input())] += 1

for i in d.values():
    if i % 2 == 1:
        cnt += 1

print(cnt)
