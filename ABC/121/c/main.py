from collections import defaultdict

n, m = map(int, input().split())
ls = []

for _ in range(n):
    a, b = map(int, input().split())
    ls.append([a, b])

ls.sort()
i = 0
price = 0

# 超えた部分を覚えておく必要があるからだるい
for num in range(n):
    i += ls[num][1]
    price += ls[num][0]*ls[num][1]
    num1 = num
    if i > m:
        break

now_cnt = i - ls[num1][1]
answer = price - ls[num1][0]*ls[num1][1] + (m - now_cnt)*ls[num1][0]

print(answer)
