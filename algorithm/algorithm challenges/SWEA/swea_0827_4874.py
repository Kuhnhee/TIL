T = int(input())

for t in range(1,T+1):
    row = input().split()

    stack = []

    answer = 0
    for c in row:
        if c.isdigit():
            stack.append(c)

        else:
            if c == '.':
                if len(stack) > 1:
                    answer = 'error'
                break

            if len(stack) < 2:
                answer = 'error'
                break
            
            first = stack.pop()
            second = stack.pop()
            
            if c == '-':
                stack.append(str(int(second)-int(first)))

            elif c =='+':
                stack.append(str(int(second)+int(first)))

            elif c == '*':
                stack.append(str(int(second)*int(first)))

            elif c == '/':
                stack.append(str(int(second)//int(first)))

    if answer != 'error':
        answer = int(float(stack[0]))

    print('#{} {}'.format(t, answer))