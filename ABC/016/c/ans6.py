import heapq

n, m = map(int, input().split())
sns = [None]+[[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    sns[a].append((1, b))
    sns[b].append((1, a))
INF = 10**9


def dijkstra(init_v):
    tasks = [(0, init_v)]
    dist = [INF]*(n+1)
    dist[init_v] = 0
    while tasks:
        d, v = heapq.heappop(tasks)
        if dist[v] < d:
            continue
        for d2, v2 in sns[v]:
            if dist[v2] <= dist[v]+d2:
                continue
            dist[v2] = dist[v]+d2
            heapq.heappush(tasks, (dist[v2], v2))
    return dist[1:]


for i in range(1, n+1):
    total = sum(1 for x in dijkstra(i) if x == 2)
    print(total)
