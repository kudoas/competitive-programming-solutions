# 部分区間の和がk以上になる最小の長さを求めよ
A = [1, 2, 3, 21, 4, 2, 1, 56, 3, 2, 133, 34, 4]
k = 10

n = len(A)
right = 0
INF = 10**18
res = INF
sum = 0
for left in range(n):
    # [left, right)の総和がk以上となるrightの最小値
    while (right < n and sum < k):
        sum += A[right]
        right += 1
    if sum < k:
        break
    print(left, right, sum)
    res = min(res, right-left)
    if right == left:
        right += 1
    else:
        sum -= A[left]

if res < n+1:
    ans = res
else:
    ans = 0
print(ans)
