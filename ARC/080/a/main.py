n = int(input())
A = list(map(int, input().split()))

checker = []
for a in A:
    cnt = 0
    if a % 2 == 0:
        cnt = 1
    if a % 4 == 0:
        cnt += 1
    checker.append(cnt)

count_2 = checker.count(2)
count_1 = checker.count(1)
count_0 = checker.count(0)

if (count_0 <= count_2+1 and count_0 + count_1 <= count_2 + 1) or count_0 == count_2:
    answer = 'Yes'
else:
    answer = 'No'

print(answer)
