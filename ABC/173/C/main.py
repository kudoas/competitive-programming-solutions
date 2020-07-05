from itertools import combinations

h, w, K = list(map(int, input().split()))
H = [i for i in range(h)]
W = [i for i in range(w)]
grid = [list(input()) for _ in range(h)]
ans = 0
for i in range(h+1):
    for hv in combinations(H, i):
        for j in range(w+1):
            for wv in combinations(W, j):
                cnt = 0
                for k in hv:
                    for l in wv:
                        if grid[k][l] == "#":
                            cnt += 1
                if cnt == K:
                    ans += 1
print(ans)
