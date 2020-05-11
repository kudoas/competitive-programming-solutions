from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
num_ls = [i for i in range(1, m+1)]

comb = combinations_with_replacement(num_ls, n)
ans = 0
for v in comb:
    cnt = 0
    for a, b, c, d in abcd:
        if v[b-1] - v[a-1] == c:
            cnt += d
    ans = max(ans, cnt)

print(ans)
