from collections import deque

h, w = map(lambda x: int(x)+2, input().split())
MAZE = ['#'*w]
for _ in range(h-2):
    MAZE.append('#'+input()+'#')
else:
    MAZE.append('#'*w)

start = []
for i in range(h):
    for j in range(w):
        if MAZE[i][j] == ".":
            start.append((i, j))


# # BFS: 汎用的だけどこれだと間に合わない
# def bfs(start):
#     i, j = start
#     INF = 10**18
#     dist = [[INF] * w for _ in range(h)]
#     dist[i][j] = 0
#     next_v = deque([start])
#     visited = set()
#     while next_v:
#         i, j = next_v.popleft()
#         direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for di, dj in direction:
#             x, y = i+di, j+dj
#             if MAZE[x][y] == "#":
#                 continue
#             if (x, y) in visited:
#                 continue
#             dist[x][y] = dist[i][j] + 1
#             visited.add((i, j))
#             next_v.append((x, y))
#     return dist


def bfs(start):
    i, j = start
    INF = 10**18
    dist = [[INF] * w for _ in range(h)]
    dist[i][j] = 0
    next_v = deque([start])
    while next_v:
        i, j = next_v.popleft()
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for di, dj in direction:
            x, y = i+di, j+dj
            if MAZE[x][y] == "#":
                continue
            if dist[x][y] <= dist[i][j] + 1:
                continue
            dist[x][y] = dist[i][j] + 1
            next_v.append((x, y))
    return dist


ans = 0
for s1 in start:
    r = bfs(s1)
    for s2 in start:
        ans = max(ans, r[s2[0]][s2[1]])

print(ans)
