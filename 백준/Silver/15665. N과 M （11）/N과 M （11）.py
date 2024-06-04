import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
q = deque()

def dfs():
    if len(q) == M:
        print(*q)
        return
    pre = 0
    for i in range(N):
        if pre != nums[i]:
            q.append(nums[i])
            pre = nums[i]
            dfs()
            q.pop()

dfs()