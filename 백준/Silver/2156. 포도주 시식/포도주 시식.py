import sys

n = int(sys.stdin.readline())

wine = [0] * 10001 # 인덱스 1 부터 사용
for i in range(1, n+1):
    wine[i] = int(sys.stdin.readline())

dp = [0] * (n+1)

# 초기화
dp[1] = wine[1]

if n >= 2:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2] + wine[i], dp[i-1], dp[i-3] + wine[i-1] + wine[i])

print(dp[n])

