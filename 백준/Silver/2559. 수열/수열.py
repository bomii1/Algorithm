import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tem = list(map(int, input().split()))

s = []
s.append(sum(tem[:K]))

for i in range(N-K):
    s.append(s[i] - tem[i] + tem[K+i])

print(max(s))