from copy import deepcopy

n = int(input())
ls = list(input().split())
C1 = []
for s in ls:
    C1.append((s[0], s[1]))
C2 = deepcopy(C1)


# bubble_sort: 2d
def bubble_sort(ls):
    n = len(ls)
    for _ in range(n):
        for j in range(n-1):
            if ls[j][1] > ls[j+1][1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


# selection_sort: 2d
def selection_sort(ls):
    n = len(ls)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if ls[j][1] < ls[minj][1]:
                minj = j
        if minj != i:
            ls[i], ls[minj] = ls[minj], ls[i]
    return ls


ans1 = []
ans2 = []
for c in bubble_sort(C1):
    ans1.append(c[0]+c[1])
for c in selection_sort(C2):
    ans2.append(c[0]+c[1])
print(*ans1)
print('Stable')
print(*ans2)
if ans1 == ans2:
    print('Stable')
else:
    print('Not stable')
