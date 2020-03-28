N = int(input())
A = [0] + [int(input()) for _ in range(N)]

# ボタンを押しまくらない方法
x = 1
visited = set([1])
answer = 0


while True:
    x = A[x]
    if x in visited:
        answer = -1
        break
    visited.add(x)
    answer += 1
    if x == 2:
        break

print(answer)
