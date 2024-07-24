import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        self.items.pop()

    def top(self):
        try:
            self.items[-1]
        except IndexError:
            print('Stack is empty')

    def __len__(self):
        return len(self.items)

k = int(input())
stack = Stack()

for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.push(num)
print(sum(stack.items))
