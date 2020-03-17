n = int(input())


def dfs(n, s):
    if n == 0:
        print(s)
    else:
        for c in ['a', 'b', 'c']:
            dfs(n-1, s+c)


dfs(n, '')
