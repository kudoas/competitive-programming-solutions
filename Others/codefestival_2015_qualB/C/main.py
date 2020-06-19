n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if n < m:
    print('NO')
    exit()
A.sort(reverse=True)
B.sort(reverse=True)
for a, b in zip(A, B):
    if a < b:
        print('NO')
        break
else:
    print('YES')
