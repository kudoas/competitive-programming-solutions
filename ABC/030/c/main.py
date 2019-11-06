import bisect

inf = float('inf')

n, m = map(int, input().split())
x, y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

while True:
    ab = bisect.bisect_left(B, A[0]+x)
    if ab <= len(B)-1:
        ba = bisect.bisect_left(A, B[ab]+y)
        print(A[ba])
        break
    break

print(B[ab])
