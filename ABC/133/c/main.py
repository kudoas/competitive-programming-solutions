L, R = map(int, input().split())

ans = 2018
for i in range(L, R):
    for j in range(i+1, R+1):
        cnt = i*j % 2019
        if cnt == 0:
            print(0)
            exit()
        ans = min(cnt, ans)

print(ans)
