n, h = map(int, input().split())
A = [0]*n
B = [0]*n
for i in range(n):
    A[i], B[i] = map(int, input().split())

max_a = max(A)
B = [b for b in B if b > max_a]
B.sort(reverse=True)

answer = 0
for b in B:
    if h <= 0:
        break
    h -= b
    answer += 1
if h > 0:
    answer += -(-h//max_a)

print(answer)
