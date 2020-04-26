bingo = [list(map(int, input().split())) for _ in range(3)]
ls = [int(input()) for _ in range(int(input()))]

for i in range(3):
    for j in range(3):
        if bingo[i][j] in ls:
            bingo[i][j] = 1
        else:
            bingo[i][j] = 0

if sum(bingo[0]) == 3 or sum(bingo[1]) == 3 or sum(bingo[2]) == 3:
    print('Yes')
    exit()

if sum(bingo[i][0] for i in range(3)) == 3 or sum(bingo[i][1] for i in range(3)) == 3 or sum(bingo[i][2] for i in range(3)) == 3:
    print('Yes')
    exit()

if bingo[0][0] + bingo[1][1] + bingo[2][2] == 3 or bingo[0][2] + bingo[1][1] + bingo[2][0] == 3:
    print('Yes')
    exit()

print('No')
