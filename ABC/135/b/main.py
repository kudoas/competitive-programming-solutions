n = int(input())
P = list(map(int, input().split()))
sP = sorted(P)
cnt = 0

for i in range(n):
    if P[i] != sP[i]:
        cnt += 1

print('YES' if cnt <= 2 else 'NO')
