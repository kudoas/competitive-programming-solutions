matrix = [list(input().split()) for _ in range(4)]

for i in reversed(range(4)):
    for j in reversed(range(4)):
        print(matrix[i][j], end=' ')
    print()
