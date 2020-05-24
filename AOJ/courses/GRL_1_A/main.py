# import heapq

# n, e, r = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(e):
#     s, t, d = map(int, input().split())
#     edges[s].append((t, d))
# INF = 10**18
# dist = [INF]*n

# while next_v:
#     v1 = next_v.popleft()
#     for v2, c in edges[v1]:
