N, T = map(int, input().split())

l = []

for i in range(N):
    a = list(map(int, input().split()))
    if a[1] <= T:
        l.append(a[0])

print('TLE' if len(l) == 0 else min(l))
