n = int(input())
_max, *A = sorted(list(map(int, input().split())), reverse=True)

medium = _max / 2

start = A[0]
for a in A[1:]:
    if abs(medium-start) > abs(medium-a):
        start = a

print(_max, start)
