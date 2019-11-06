n = int(input())
cnt = 0

for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == 'JPY':
        cnt += x
    else:
        cnt += x*380000

print(cnt)
