n = int(input())
d, x = map(int, input().split())
cnt = 0

for _ in range(n):
    a = int(input())
    for i in range(100):
        if a*i+1 <= d:
            cnt += 1
        else:
            break

print(cnt+x)
