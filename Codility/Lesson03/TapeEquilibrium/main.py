# small case
def solution(A):
    n = len(A)
    left = 0
    right = sum(A)
    ans = abs(left-right)
    for i in range(n):
        left += A[i]
        right -= A[i]
        diff = abs(left - right)
        ans = min(ans, diff)
    return ans
