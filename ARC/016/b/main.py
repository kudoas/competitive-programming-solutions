N = int(input())

# X: カウント1､ ○: 続いているカウント1
ls = [list(input()) for _ in range(N)]
ll = []

for i in range(9):
    lll = []
    for j in range(N):
        lll.append(ls[j][i])
    ll.append(['.']+lll)

cnt = 0

for i in range(9):
    for j in range(N):
        if ll[i][j] != ll[i][j+1] == 'o':
            cnt += 1
        elif ll[i][j+1] == 'x':
            cnt += 1

print(cnt)
