import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tem = list(map(int, input().split()))

s = [0] * N
s[K-1] = sum(tem[:K])

MAX = s[K-1]
temIndex = 0

if N == K:
    print(sum(tem))
else:
    for i in range(K, N):
        s[i] = s[i-1] - tem[temIndex] + tem[i]
        temIndex += 1

        if MAX < s[i]:
            MAX = s[i]
    print(MAX)