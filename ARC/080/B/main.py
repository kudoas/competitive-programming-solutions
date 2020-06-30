h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
grid = []
for i, num in enumerate(A, 1):
    grid += [i]*num


def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


ans = list(split_list(grid, w))
for i in range(h):
    if i % 2 == 0:
        print(*ans[i])
    else:
        print(*ans[i][::-1])
