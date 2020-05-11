h, w = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(map(int, input())))
ans = [[0]*w for _ in range(h)]

for i in range(h-2):
    for j in range(1, w-1):
        x = board[i][j]
        ans[i+1][j] = x
        board[i+1][j+1] -= x
        board[i+1][j-1] -= x
        board[i+2][j] -= x

for row in ans:
    print(*row, sep='')
