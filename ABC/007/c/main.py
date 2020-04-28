from collections import deque

h, w = map(int, input().split())
start = tuple(map(lambda x: int(x)-1, input().split()))
goal = tuple(map(lambda x: int(x)-1, input().split()))
maze = [input() for _ in range(h)]
INF = 10**18
# マス分
distance = [[INF] * w for _ in range(h)]
i, j = start
distance[i][j] = 0

# タスク管理
next_v = deque([start])
# O(h*W+h*w*4)
# O(V+E)
while next_v:
    i, j = next_v.popleft()
    dirction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for di, dj in dirction:
        x, y = i+di, j+dj
        if maze[x][y] == "#":
            continue
        # 戻らない処理
        if distance[x][y] <= distance[i][j] + 1:
            continue
        distance[x][y] = distance[i][j] + 1
        # distance[x][y] = min(distance[x][y], distance[i][j] + 1)
        next_v.append((x, y))

i, j = goal
print(distance[i][j])
