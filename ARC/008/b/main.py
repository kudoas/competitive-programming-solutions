from collections import Counter

n, m = map(int, input().split())
name = list(input())
kit = list(input())

cnt_name = Counter(name)
cnt_kit = Counter(kit)

for n in name:
    if n not in kit:
        print(-1)
        exit()

ans = 0
for k, v in cnt_name.items():
    ans = max(ans, -(-v//cnt_kit[k]))

print(ans)
