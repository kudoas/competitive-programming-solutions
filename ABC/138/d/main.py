import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, q = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

count = [0]*n
for i in range(q):
    p, x = map(int, input().split())
    count[p-1] += x


def dfs(v, parent):
    for v2 in edges[v]:
        if v2 == parent:
            continue
        count[v2] += count[v]
        dfs(v2, v)


dfs(0, None)
print(*count)
