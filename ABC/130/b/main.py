n, x = map(int, input().split())
L = list(map(int, input().split()))
D = [0]
cnt = 0

for i in range(n):
    cnt += L[i]
    if cnt <= x:
        D.append(cnt)

print(len(D))
