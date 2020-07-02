E = set(map(int, input().split()))
b = int(input())
L = set(map(int, input().split()))
se = E & L
bonus = False
if len(se) == 5:
    for l in L:
        if l not in E and l == b:
            bonus = True
cnt = len(se)
if cnt == 6:
    ans = 1
elif cnt == 5 and bonus:
    ans = 2
elif cnt == 5:
    ans = 3
elif cnt == 4:
    ans = 4
elif cnt == 3:
    ans = 5
else:
    ans = 0
print(ans)
