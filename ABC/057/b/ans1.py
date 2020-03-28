n, m = map(int, input().split())

ab_ls = [[int(x) for x in input().split()] for _ in range(n)]
cd_ls = [[int(x) for x in input().split()] for _ in range(n)]


answer = []
for ab in ab_ls:
    min_distance = float('inf')
    target = 0
    for j, cd in enumerate(cd_ls, 1):
        x = abs(ab[0]-cd[0]) + abs(ab[1]-cd[1])
        if min_distance > x:
            min_distance = x
            target = j
    answer.append(target)

print(*answer, sep='\n')
