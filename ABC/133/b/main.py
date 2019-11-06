from itertools import combinations

n, D = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


for a, b in combinations(ls, 2):
    l = 0
    for d in range(D):
        l += (a[d]-b[d])**2
    if l ** 0.5 == int(l ** 0.5):
        cnt += 1

print(cnt)
