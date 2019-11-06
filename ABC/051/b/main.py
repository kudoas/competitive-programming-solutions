k, s = map(int, input().split())
cnt = 0

# 条件に合うzは一つしかない
for x in range(k+1):
    for y in range(k+1):
        if s-k <= x+y <= s:
            cnt += 1

print(cnt)
