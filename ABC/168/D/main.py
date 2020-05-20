# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# edges = [[]for _ in range(n)]
# for _ in range(m):
#     a, b = map(lambda x: int(x)-1, input().split())
#     edges[a].append(b)
#     edges[b].append(a)

# next_v = deque([0])
# prev = [-1]*n
# while next_v:
#     v = next_v.popleft()
#     for v2 in edges[v]:
#         if prev[v2] != -1:
#             continue
#         prev[v2] = v+1
#         next_v.append(v2)

# print('Yes')
# for x in prev[1:]:
#     print(x)


# 俺はBFSが実装できるようになる！！！
from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)

next_v = deque([0])
INF = 10**18
# 0からの距離を保存する部分
dist = [INF]*n
dist[0] = 0
# 1からnまででどこからきたのか記述する
prev = [-1]*n
while next_v:
    v1 = next_v.popleft()
    for v2 in edges[v1]:
        if dist[v2] != INF:
            continue
        dist[v2] = dist[v1] + 1
        prev[v2] = v1
        next_v.append(v2)

if min(prev[1:]) == -1:
    print('No')
else:
    print('Yes')
    ans = [x+1 for x in prev[1:]]
    print(*ans, sep='\n')
