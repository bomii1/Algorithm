import sys
input = sys.stdin.readline

N = int(input())

RGB = []
RGB.append(0)
for i in range(N):
    RGB.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N+1)]
dp[1][0], dp[1][1], dp[1][2] = [RGB[1][0], RGB[1][1], RGB[1][2]]

for i in range(2, N+1):
    R = RGB[i][0]
    G = RGB[i][1]
    B = RGB[i][2]

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))
