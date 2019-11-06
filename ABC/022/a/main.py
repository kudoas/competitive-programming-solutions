n, s, t = map(int, input().split())
cnt = w = 0

for _ in range(n):
    w += int(input())
    cnt += s <= w <= t

print(cnt)
