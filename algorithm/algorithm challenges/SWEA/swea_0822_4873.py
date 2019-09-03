T = int(input())

for t in range(1,T+1):
    data = input()
    stack = []
    for c in data:
        if len(stack)!=0 and stack[-1] == c:
            stack.pop()
            continue
        else:
            stack.append(c)
    print('#{} {}'.format(t, len(stack)))