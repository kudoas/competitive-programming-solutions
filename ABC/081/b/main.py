n = int(input())
aa = list(map(int, input().split()))

k = float('inf')

for i in range(n):
    j = 0
    while aa[i] % 2 == 0:
        aa[i] = aa[i]/2
        j += 1
    k = min(j, k)

print(k)
