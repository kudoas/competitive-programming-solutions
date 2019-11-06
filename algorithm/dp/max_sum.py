def max_sum(n, a):
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = max(dp[i], dp[i]+a[i])
    return dp[n]


a = [1, 2, 3, 4, 2, 2, -1, 2, 3, -3, -2]
r = max_sum(len(a), a)  # 19
