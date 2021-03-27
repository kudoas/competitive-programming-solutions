n = int(input())
S = list(map(int, input().split()))  # sorted
q = int(input())
T = list(map(int, input().split()))


def binary_search(A: list, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid + 1
        else:
            right = mid
    return 'NOT_FOUND'


cnt = 0
for t in T:
    if binary_search(S, t) != 'NOT_FOUND':
        cnt += 1

print(cnt)
