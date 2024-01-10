import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            print(self.items[-1])
            self.items.pop()
        except IndexError:
            print(-1)

    def top(self):
        try:
            print(self.items[-1])
        except IndexError:
            print(-1)

    def empty(self):
        if len(self.items) == 0:
            print(1)
        else:
            print(0)

    def size(self):
        print(len(self.items))

s = Stack()

n = int(sys.stdin.readline())
stackList = [sys.stdin.readline().strip() for i in range(n)]


for i in range(n):
    if stackList[i][1] == 'u': # push
        s.push(stackList[i][5:])
    elif stackList[i][0] == 'p' and stackList[i][1] == 'o': # pop
        s.pop()
    elif stackList[i][0] == 't': # top
        s.top()
    elif stackList[i][0] == 's': # size
        s.size()
    elif stackList[i][0] == 'e': # empty
        s.empty()