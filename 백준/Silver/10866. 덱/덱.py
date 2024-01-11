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

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        d.push_front(int(cmd[1]))
    elif cmd[0] == 'push_back':
        d.push_back(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        d.pop_front()
    elif cmd[0] == 'pop_back':
        d.pop_back()
    elif cmd[0] == 'size':
        d.size()
    elif cmd[0] == 'empty':
        d.empty()
    elif cmd[0] == 'front':
        d.front()
    elif cmd[0] == 'back':
        d.back()