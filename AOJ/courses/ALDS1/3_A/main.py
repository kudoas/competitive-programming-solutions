ls = list(input().split())


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()


stack = Stack()
for s in ls:
    if s in ['+', '-', '*']:
        v2 = stack.pop()
        v1 = stack.pop()
        stack.push(str(eval(v1+s+v2)))
    else:
        stack.push(s)
print(stack.stack[0])
