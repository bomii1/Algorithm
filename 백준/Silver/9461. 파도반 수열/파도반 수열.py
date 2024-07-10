import sys
input = sys.stdin.readline
def dp(N):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    if N <= 5:
        return dp[N]

    for j in range(6, N+1):
        dp[j] = dp[j-1] + dp[j-5]
    return dp[N]

T = int(input())
N = [int(input()) for __ in range(T)]

for i in range(T):
    print(dp(N[i]))