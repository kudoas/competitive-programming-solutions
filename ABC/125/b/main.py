n = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
cnt = 0
ls = []

for i in range(n):
    ls.append(V[i] - C[i])

for l in ls:
    if l >= 0:
        cnt += l
