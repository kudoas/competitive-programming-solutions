import itertools

# 組み合わせ(iterableなobjectを返す)
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dist = []

for (x1, y1), (x2, y2) in itertools.combinations(ls, 2):
    dist.append((x1-x2)**2 + (y1-y2)**2)

print(max(dist)**.5)
