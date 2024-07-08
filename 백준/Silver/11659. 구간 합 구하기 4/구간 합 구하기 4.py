import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = arr[0]

for j in range(2, N+1):
    dp[j] += dp[j-1] + arr[j-1]

for i in range(M):
    start, end = map(int, input().split(' '))
    print(dp[end] - dp[start-1])
