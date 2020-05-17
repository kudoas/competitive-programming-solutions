from itertools import product

n, k = map(int, input().split())
T = [tuple(map(int, input().split())) for _ in range(n)]

for i in product([i for i in range(k)], repeat=n):
    ans = 0
    for j in range(n):
        ans ^= T[j][i[j]]
    if ans == 0:
        print('Found')
        break
else:
    print('Nothing')
