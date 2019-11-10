n, a, b = map(int, input().split())
ans = 0

for i in range(1, n+1):
    cnt = 0
    for j in range(len(str(i))):
        cnt += int(str(i)[j])
    if a <= cnt <= b:
        ans += i

print(ans)
