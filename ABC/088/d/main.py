from collections import deque

h, w = map(lambda x: int(x)+2, input().split())
MAZE = ['#'*w]
for _ in range(h-2):
    MAZE.append('#'+input()+'#')
else:
    MAZE.append('#'*w)

total = 0
for i in range(h):
    for j in range(w):
        if MAZE[i][j] == '.':
            total += 1

# よく考えたらBFSでOKだった
i, j = (1, 1)
INF = 10**18
dist = [[INF] * w for _ in range(h)]
dist[i][j] = 1
next_v = deque([[i, j]])
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

last = dist[h-2][w-2]
if last != INF:
    ans = total - last
else:
    ans = -1
print(ans)
