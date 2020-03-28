k, n = map(int, input().split())
A = list(map(int, input().split()))


start_diff = A[0] + k - A[-1]
diff = [start_diff]
answer = 0
start = A[0]

for i in range(1, n):
    diff.append(A[i] - start)
    start = A[i]

# print(diff)
# print(start_diff)

answer = sum(diff) - max(diff)
print(answer)
