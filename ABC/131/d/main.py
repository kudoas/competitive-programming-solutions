n = int(input())

ab = [tuple(map(int, (input().split()))) for _ in range(n)]
ab = sorted(ab, key=lambda x: x[1])

timer = 0
for a, b in ab:
    timer += a
    if timer > b:
        print('No')
        exit()

print('Yes')
