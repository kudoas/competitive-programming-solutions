import sys
input = sys.stdin.readline

n, q = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

count = [0]*n
for _ in range(q):
    p, x = map(int, input().split())
    count[p-1] += x

stack = [0]
visited = [0]*n
while stack:
    v = stack.pop()
    visited[v] = 1
    for v2 in edges[v]:
        if visited[v2]:
            continue
        count[v2] += count[v]
        stack.append(v2)

print(*count)
