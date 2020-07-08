c = int(input())
N, M, L = 0, 0, 0
for _ in range(c):
    n, m, l = sorted(list(map(int, input().split())))
    N = max(N, n)
    M = max(M, m)
    L = max(L, l)
print(N*M*L)
