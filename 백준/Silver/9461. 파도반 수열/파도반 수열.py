import sys
input = sys.stdin.readline
def dp(N):
    dp = [0, 1, 1, 1, 2, 2]
    
    if N <= 5:
        return dp[N]
    for j in range(6, N+1):
        dp.append(dp[j-1] + dp[j-5])
    return dp[N]

T = int(input())
N = [int(input()) for __ in range(T)]

for i in range(T):
    print(dp(N[i]))