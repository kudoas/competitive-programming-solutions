n, l = map(int, input().split())
amida = [['|', ' '] + list(input()) + ['|', ' '] for _ in range(l)]
goal = [' ']*2 + list(input()) + [' ']*2
now = goal.index('o')
for row in amida[::-1]:
    if row[now-1] == "-":
        now -= 2
    elif row[now+1] == "-":
        now += 2
ans = now//2
print(ans)
