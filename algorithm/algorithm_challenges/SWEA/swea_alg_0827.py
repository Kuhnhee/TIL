for t in range(1,11):

    L = int(input())
    row = input()
    postfix = ""
    stack = []
    for c in row:
        if c.isdigit():
            postfix += c
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            elif c == '*':
                stack.append(c)
            elif c == '+':
                while stack[-1] == '*':
                    postfix += stack.pop()
                stack.append(c)

    # print(postfix)

    stack = []
    for c in postfix:
        if c.isdigit():
            stack.append(c)
        elif c == '*':
            first = stack.pop()
            second = stack.pop()
            stack.append(str(int(first)*int(second)))
        elif c == '+':
            first = stack.pop()
            second = stack.pop()
            stack.append(str(int(first)+int(second)))

    print('#{} {}'.format(t, int(stack[0])))
