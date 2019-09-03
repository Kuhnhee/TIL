T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for e in range(E):
        edges.append(list(map(int,input().split())))
    S,G = map(int,input().split())

    stack = []
    for e in edges:
        if e[0] == S:
            stack.append(e[1])

    answer = 0
    while stack:

        if G in stack:
            answer = 1
            break

        pos = stack.pop()

        for e in edges:
            if e[0] == pos:
                stack.append(e[1])

    print('#{} {}'.format(t, answer))