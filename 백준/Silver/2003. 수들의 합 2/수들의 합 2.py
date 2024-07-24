import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
interval_sum = 0
end = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += A[end]
        end += 1
    if interval_sum == M:
        cnt += 1
    interval_sum -= A[start]
print(cnt)




