N = int(input())
H = list(map(int, input().split()))

cnt = 0
before = 0

for i in range(N):
    if before < H[i]:
        cnt += H[i] - before
    before = H[i]

print(cnt)
