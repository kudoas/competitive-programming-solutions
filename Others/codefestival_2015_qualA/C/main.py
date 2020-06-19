n, t = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(n)]
cost = 0
profit = []
for a, b in AB:
    profit.append(a-b)
    cost += a
cost -= t
if cost <= 0:
    print(0)
    exit()
profit.sort(reverse=True)
ans = 0
for p in profit:
    ans += 1
    cost -= p
    if cost <= 0:
        print(ans)
        break
else:
    print(-1)
