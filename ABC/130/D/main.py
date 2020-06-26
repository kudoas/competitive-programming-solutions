# n, k = map(int, input().split())
# A = list(map(int, input().split()))
# S = [0]*(n+1)
# for i in range(n):
#     S[i+1] += S[i] + A[i]

# left = 0
# ans = 0
# for right in range(n+1):
#     while S[right]-S[left] >= k:
#         left += 1
#     ans += left
# print(ans)

n, k = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
ans = 0
right = 0
for left in range(n):
    # [left, right)の総和がk以上となるrightの最小値までright++
    while (right < n and sum < k):
        sum += A[right]
        right += 1
    print(left, right, sum)
    if sum < k:
        break
    ans += 1
    if right == left:
        right += 1
    else:
        sum -= A[left]
print(ans)
