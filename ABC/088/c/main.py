ls = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

for i in range(3):
    for j in range(3):
        if ls[i % 3][j % 3] - ls[i % 3][(j+1) % 3] == ls[(i+1) % 3][j % 3] - ls[(i+1) % 3][(j+1) % 3]:
            cnt += 1

print('Yes' if cnt == 9 else 'No')
