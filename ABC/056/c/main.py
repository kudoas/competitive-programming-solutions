x = int(input())

cnt = 0

for i in range(1, 100000000):
    cnt += i
    if cnt >= x:
        ans = i
        break

print(ans)
