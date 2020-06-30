n = int(input())
A = list(map(int, input().split()))
cnt4 = 0
cnt2 = 0
other = 0
for a in A:
    if a % 4 == 0:
        cnt4 += 1
        continue
    if a % 2 == 0:
        cnt2 += 1
    else:
        other += 1
if cnt4+1 >= cnt2 + other or cnt4 >= other:
    print('Yes')
else:
    print('No')
