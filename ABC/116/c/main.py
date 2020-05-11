# n = int(input())
# H = list(map(int, input().split()))
# ans = H[0]
# for i in range(1, n):
#     ans += max(0, H[i]-H[i-1])
# print(ans)

n = int(input())
H = list(map(int, input().split()))
ans = 0
while sum(H) > 0:
    prev = 0
    split = 0
    for h in H:
        if prev == 0 and h != 0:
            split += 1
        prev = h
    ans += split
    H = [h-1 if h > 0 else 0 for h in H]

print(ans)
