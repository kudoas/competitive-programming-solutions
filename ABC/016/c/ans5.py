import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
sns = [[]for _ in range(n)]
for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    sns[a].append(b)
    sns[b].append(a)
INF = 10**9


def make_dfs():
    dist = [INF]*n

    def dfs(v, parent, distance):
        dist[v] = distance
        for v2 in sns[v]:
            # 来た道戻るの禁止
            if v2 == parent:
                continue
            # 閉路スルー
            if dist[v2] <= distance+1:
                continue
            dfs(v2, v, distance+1)
        return dist
    return dfs


for i in range(n):
    dfs = make_dfs()
    total = sum(1 for x in dfs(i, -1, 0)if x == 2)
    print(total)
