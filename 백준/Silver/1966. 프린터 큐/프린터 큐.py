from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    input_values = list(map(int, input().split()))
    importance = deque([index, value] for index, value in enumerate(input_values))
    sorted_importance = sorted(importance, key=lambda x: x[1], reverse=True)
    find_value = importance[M]
    count = 0
    sorted_index = 0

    while importance:
        MAX = max(importance, key=lambda x: x[1])
        if MAX[1] > importance[0][1]:
            importance.append(importance.popleft())
        else:
            num = importance.popleft()
            count += 1
            sorted_index += 1
            if num == find_value:
                print(count)