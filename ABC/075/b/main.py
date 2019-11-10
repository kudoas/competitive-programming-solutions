h, w = map(int, input().split())
ss = []
ls = []

# 一回り大きくする
ss.append(['.']*(w+2))
for _ in range(h):
    ss.append(['.']+list(input())+['.'])
ss.append(['.']*(w+2))

for i in range(1, h+1):
    for j in range(1, w+1):
        if ss[i][j] == '.':
            n = (
                ss[i-1][j-1],
                ss[i-1][j],
                ss[i-1][j+1],
                ss[i][j-1],
                ss[i][j+1],
                ss[i+1][j-1],
                ss[i+1][j],
                ss[i+1][j+1],
            ).count('#')
            ss[i][j] = n
        else:
            ss[i][j] = '#'

for i in range(1, h+1):
    for j in range(1, w+1):
        print(ss[i][j], end='')
    print()
