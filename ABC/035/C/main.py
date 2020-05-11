# n, q = map(int, input().split())
# board = [0]*(n+1)
# for _ in range(q):
#     l, r = map(int, input().split())
#     board[l-1] += 1
#     board[r] += -1

# cum_sum = [0]*(n+2)
# for i in range(n+1):
#     cum_sum[i+1] += board[i] + cum_sum[i]

# answer = []
# for i in range(1, n+1):
#     if cum_sum[i] % 2 == 0:
#         answer.append(0)
#     else:
#         answer.append(1)

# print(*answer, sep='')

n, q = map(int, input().split())
board = [0]*n
for _ in range(q):
    l, r = map(int, input().split())
    board[l-1] += 1
    if r < n:
        board[r] += -1

cum_sum = [0]*(n+1)
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + board[i]
for i in range(1, n+1):
    if cum_sum[i] % 2 == 0:
        board[i-1] = 0
    else:
        board[i-1] = 1

print(*board, sep='')
