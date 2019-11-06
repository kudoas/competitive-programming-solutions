n, q = map(int, input().split())
list = [0]*n

for i in range(q):
    l, r, t = map(int, input().split())
    list[l-1:r] = [t]*(r-l+1)

print(*list, sep='\n')
