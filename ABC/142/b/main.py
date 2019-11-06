n, k = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if ls[i] >= k:
        cnt += 1

print(cnt)
