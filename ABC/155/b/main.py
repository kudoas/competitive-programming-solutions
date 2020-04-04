n = int(input())
A = list(map(int, input().split()))

bl = True
for a in A:
    if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
        bl = False
        break

print('APPROVED' if bl else 'DENIED')
