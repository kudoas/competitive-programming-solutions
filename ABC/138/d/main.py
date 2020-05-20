# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# n, q = map(int, input().split())
# edges = [[] for _ in range(n)]

# for _ in range(n-1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     edges[a].append(b)
#     edges[b].append(a)

# count = [0]*n
# for i in range(q):
#     p, x = map(int, input().split())
#     count[p-1] += x


# def dfs(v, parent):
#     for v2 in edges[v]:
#         if v2 == parent:
#             continue
#         count[v2] += count[v]
#         dfs(v2, v)


# dfs(0, None)
# print(*count)

# input = sys.stdin.readline

# n, q = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     edges[a].append(b)
#     edges[b].append(a)

# count = [0]*n
# for _ in range(q):
#     p, x = map(int, input().split())
#     count[p-1] += x

# stack = [0]
# visited = [0]*n
# while stack:
#     v = stack.pop()
#     visited[v] = 1
#     for v2 in edges[v]:
#         if visited[v2]:
#             continue
#         count[v2] += count[v]
#         stack.append(v2)

# print(*count)


# 私はDFSを書けるようになるまで諦めない！！
n, q = map(int, input().split())
edges = [[]for _ in range(n)]
count = [0]*n
for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)
for _ in range(q):
    p, x = map(int, input().split())
    count[p-1] += x

stack = [0]
INF = 10**18
counter = [INF]*n
counter[0] = count[0]
while stack:
    v1 = stack.pop()
    for v2 in edges[v1]:
        if counter[v2] != INF:
            continue
        counter[v2] = counter[v1] + count[v2]
        stack.append(v2)

print(*counter)
