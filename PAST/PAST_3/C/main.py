a, r, n = map(int, input().split())
if r == 1:
    print(a)
    exit()
total = a
num = 2
while total <= 10**9 and num < n+1:
    total *= r
    num += 1
print('large' if total > 10**9 else total)
