h, w = map(int, input().split())

ls = []

ls += [['.']*(w+2)]
for _ in range(h):
    ls += [['.'] + list(input()) + ['.']]
ls += [['.']*(w+2)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if ls[i][j] != '#':
            continue
        if ls[i][j-1] != '#' and ls[i-1][j] != '#' and ls[i+1][j] != '#' and ls[i][j+1] != '#':
            print('No')
            exit()

print('Yes')
