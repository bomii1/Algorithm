T = int(input())

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(T):
    N = int(input())
    for j in range(2, N+1):
        dp[j][0], dp[j][1] = dp[j-1][0] + dp[j-2][0], dp[j-1][1] + dp[j-2][1]
    print(dp[N][0], dp[N][1])