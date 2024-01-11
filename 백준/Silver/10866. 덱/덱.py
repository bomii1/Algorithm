import sys

class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, val):
        tmp = []
        tmp.append(val)
        tmp += self.items
        self.items = tmp

    def push_back(self, val):
        self.items.append(val)

    def pop_front(self):
        try:
            print(self.items[0])
            self.items.pop(0)
        except IndexError:
            print(-1)

    def pop_back(self):
        try:
            print(self.items[-1])
            self.items.pop()
        except IndexError:
            print(-1)

    def size(self):
        print(len(self.items))

    def empty(self):
        if len(self.items) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.items) > 0:
            print(self.items[0])
        else:
            print(-1)

    def back(self):
        if len(self.items) > 0:
            print(self.items[-1])
        else:
            print(-1)

d = Deque()

n = int(sys.stdin.readline())
DequeList = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    if DequeList[i][1] == 'u' and DequeList[i][5] == 'f':
        d.push_front(DequeList[i][11:])
    elif DequeList[i][1] == 'u' and DequeList[i][5] == 'b':
        d.push_back(DequeList[i][10:])
    elif DequeList[i][1] == 'o' and DequeList[i][4] == 'f':
        d.pop_front()
    elif DequeList[i][1] == 'o' and DequeList[i][4] == 'b':
        d.pop_back()
    elif DequeList[i][0] == 'f':
        d.front()
    elif DequeList[i][0] == 'b':
        d.back()
    elif DequeList[i][0] == 'e':
        d.empty()
    elif DequeList[i][0] == 's':
        d.size()