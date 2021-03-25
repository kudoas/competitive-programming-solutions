# stack
# https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-stacks

ls = list(input().split())
stack = []
operators = ['+', '-', '*']
for l in ls:
    if l in operators:
        b = int(stack.pop())
        a = int(stack.pop())
        if l == "+":
            stack.append(a + b)
        elif l == "-":
            stack.append(a - b)
        elif l == '*':
            stack.append(a * b)
    else:
        stack.append(l)

print(stack.pop())
