import sys

class Queue:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            print(self.items[0])
            self.items.pop(0)
        except IndexError:
            print(-1)

    def front(self):
        try:
            print(self.items[0])
        except IndexError:
            print(-1)
    def back(self):
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

q = Queue()

n = int(sys.stdin.readline())
stackList = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    if stackList[i][1] == 'u': # push
        q.push(stackList[i][5:])
    elif stackList[i][0] == 'p' and stackList[i][1] == 'o': # pop
        q.pop()
    elif stackList[i][0] == 'f': # front
        q.front()
    elif stackList[i][0] == 'b': # back
        q.back()
    elif stackList[i][0] == 's': # size
        q.size()
    elif stackList[i][0] == 'e': # empty
        q.empty()