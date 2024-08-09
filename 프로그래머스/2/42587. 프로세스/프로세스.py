from collections import deque
import sys

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)

    while priorities:
        MAX = max(priorities)
        front = priorities.popleft()
        location -= 1

        if front == MAX:
            answer += 1
            if location < 0:
                return answer
        else:
            priorities.append(front)
            if location < 0:
                location = len(priorities) - 1
    return answer
