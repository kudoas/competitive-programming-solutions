B = list(map(str, input().split()))
n = int(input())
A = [input() for _ in range(n)]
for _ in range(n):
    for i in range(n-1):
        if len(A[i]) > len(A[i+1]):
            A[i], A[i+1] = A[i+1], A[i]
        elif len(A[i]) < len(A[i+1]):
            continue
        else:
            for a, b in zip(A[i], A[i+1]):
                if a == b:
                    continue
                if B.index(a) < B.index(b):
                    break
                if B.index(a) > B.index(b):
                    A[i], A[i+1] = A[i+1], A[i]
                    break
for a in map(int, A):
    print(a)
