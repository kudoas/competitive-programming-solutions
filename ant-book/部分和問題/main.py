n = 5
a = [1, 2, 4, 7, 8]
k = 15


def dfs(i, sum):
    if n == i:
        return sum == k
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum+a[i]):
        return True
    return False


if dfs(0, 0):
    print('Yes')
else:
    print('No')
