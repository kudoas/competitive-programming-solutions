n = int(input())
abc = [tuple(map(int, input().split())) for _ in range(n)]


dp = [[0, 0, 0] for _ in range(n+1)]
for i in range(n):
    for place_y in range(3):
        for place in range(3):
            if place_y != place:
                dp[i+1][place] = max(
                    dp[i+1][place], dp[i][place_y]+abc[i][place]
                )

print(max(dp[n]))
