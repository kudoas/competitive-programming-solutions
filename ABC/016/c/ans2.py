from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

n, m = map(int, input().split())
GRAPH = [[0]*n for _ in range(n)]

for i in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    GRAPH[a][b] = GRAPH[b][a] = 1

sp = floyd_warshall(csgraph_from_dense(GRAPH))

for i in range(n):
    total = sum(1 for x in sp[i] if x == 2)
    print(total)
