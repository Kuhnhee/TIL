T = int(input())

for t in range(1, T+1):

    data = input()
    stack = []
    answer = 1
    for i in data:
        if i == '{' or i == '(':
            stack.append(i)

        elif i == '}':
            if not stack:
                answer = 0
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                answer = 0
                # print('breaking')
                break
        
        elif i == ')':
            if not stack:
                answer = 0
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                answer = 0
                # print('breaking')
                break
    if stack:
        answer = 0
    print('#{} {}'.format(t, answer))