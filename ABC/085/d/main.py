from math import ceil

n, h = map(int, input().split())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

B.sort(reverse=True)
max_A = max(A)

answer = 0
for b in B:
    if max_A < b:
        h -= b
        answer += 1
    if h <= 0:
        break
if h > 0:
    answer += ceil(h/max_A)

print(answer)
