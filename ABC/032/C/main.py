n, k = map(int, input().split())
S = [int(input()) for _ in range(n)]
if 0 in S:
    print(n)
    exit()

ans = 0
right = 0
x = 1
for left in range(n):
    if left > right:
        right += 1
    while right < n and x*S[right] <= k:
        x *= S[right]
        right += 1
    ans = max(ans, right-left)
    if left != right:
        x //= S[left]
print(ans)
