n, m = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
po = total*(1/(4*m))

cnt = 0
for a in A:
    if po <= a:
        cnt += 1


print('Yes' if cnt >= m else 'No')
