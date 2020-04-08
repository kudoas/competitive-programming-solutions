n = int(input())
A = [int(x) for x in input().split()]

A.sort(reverse=True)

x = A[0]
y = 0
temp = 0

for yy in A:
    d = min(yy, x-yy)
    if d > temp:
        temp = d
        y = yy

ans = (x, y)
print(*ans)
