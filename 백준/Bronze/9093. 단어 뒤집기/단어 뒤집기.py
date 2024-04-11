import sys
from collections import deque

T = int(input())

for _ in range(T):
    sentence = sys.stdin.readline().rstrip().split(" ")

    for i in range(len(sentence)):
        for j in range(len(sentence[i])-1, -1, -1):
            print(sentence[i][j], end="")
        print(" ", end="")