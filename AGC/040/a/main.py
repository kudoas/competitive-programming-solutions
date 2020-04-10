s = input()
n = len(s)
right = [0] * (n+1)
left = [0] * (n+1)

for i in range(n):
    if s[i] == '<':
        left[i+1] = left[i] + 1

for i in range(n):
    if s[n-i-1] == '>':
        right[n-i-1] = right[n-i] + 1

ans = 0
for r, l in zip(right, left):
    ans += max(r, l)

print(ans)
