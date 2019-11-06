import bisect


n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))


cnt = 0

for b in B:
    mid = bisect.bisect_left(A, b)
    bottom = n - bisect.bisect_right(C, b)
    cnt += mid*bottom

print(cnt)
