n = int(input())
a, b, c = [list(map(int, input().split())) for _ in range(3)]
total = 0

for i in range(n):
    total += b[a[i]-1]
    if i-1 >= 0 and a[i]-a[i-1] == 1:
        total += c[a[i-1]-1]

print(total)
