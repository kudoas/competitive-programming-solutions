n = int(input())
ls = list(map(int, input().split()))
cnt = 0

for i in range(n-2):
    a, b, c = ls[i], ls[i+1], ls[i+2]
    if c > b > a or a > b > c:
        cnt += 1

print(cnt)
