import sys
from collections import deque
input = sys.stdin.readline

string = list(input().strip())

queue = deque()

def printTag(q):
    while q:
        print(q.popleft(), end='')

def printWord(q):
    while q:
        print(q.pop(), end='')

pre = 0

for x in string:
    if x == '<':
        pre = 1
        printWord(queue)
        queue.append(x)
    elif x == '>' and pre == 1:
        printTag(queue)
        print(x, end='')
        pre = 0
    elif x == ' ' and pre == 0:
        printWord(queue)
        print(x, end='')
    else:
        queue.append(x)

printWord(queue)


