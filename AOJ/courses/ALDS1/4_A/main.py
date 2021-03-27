n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def linear_search(a, n, key):
    i = 0
    a.append(key)
    while (a[i] != key):
        i += 1
    a.pop()
    return i != n


cnt = 0
for t in T:
    if linear_search(S, n, t):
        cnt += 1

print(cnt)
