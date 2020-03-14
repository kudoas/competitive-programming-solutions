N, M = map(int, input().split())
ls = [1] + [0] * (N-1)
print(ls)

for _ in range(M):
    s, c = map(int, input().split())
    if ls[s-1] != 0 and ls[s-1] != c:
        ls[s-1] = c
    else:
        print(-1)
        exit()
