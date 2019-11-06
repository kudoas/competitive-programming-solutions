n, m = map(int, input().split())
l = [0]*m

for _ in range(n):
    k, *a = map(int, input().split())
    for i in a:
        l[i-1] += 1

print(sum([1 for k in l if k == n]))
