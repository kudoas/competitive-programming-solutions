from collections import deque

n, m = map(int, input().split())
sns = [[]for _ in range(n)]
for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    sns[a].append(b)
    sns[b].append(a)
INF = float('inf')


def bfs(init_v):
    tasks = deque([init_v])
    dist = [INF]*n
    dist[init_v] = 0
    while tasks:
        v = tasks.popleft()
        for v2 in sns[v]:
            if dist[v2] <= dist[v] + 1:
                continue
            dist[v2] = dist[v]+1
            tasks.append(v2)
    return dist


for i in range(n):
    total = sum(1 for x in bfs(i) if x == 2)
    print(total)
