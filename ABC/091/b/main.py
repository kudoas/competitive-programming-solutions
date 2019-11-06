from collections import defaultdict
d = defaultdict(int)

N = int(input())
for _ in range(N):
    d[input()] += 1

M = int(input())
for _ in range(M):
    d[input()] -= 1

answer = max(d.values())
if answer < 0:
    answer = 0
print(answer)
