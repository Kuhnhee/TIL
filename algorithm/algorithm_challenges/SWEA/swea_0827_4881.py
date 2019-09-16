
T = int(input())

for t in range(1, T+1):
    N = int(input())

    field = []
    for n in range(N):
        field.append(list(map(int,input().split())))

    stack = []
    for n in range(N):
        stack.append([0,n])

    visited_col = []
    visited_path = []
    current_min = 1000
    summation = 0
    depth = 0
    while stack:
        pos = stack.pop()

        if visited_path and visited_col and pos[0] <= depth:
            backtrack = depth - pos[0]
            for i in range(backtrack+1):
                summation -= field[visited_path[-1][0]][visited_path[-1][1]]
                visited_path.pop()
                visited_col.pop()
            
        visited_path.append(pos)
        visited_col.append(pos[1])
        summation += field[pos[0]][pos[1]]
        depth = pos[0]

        #backtrack
        if summation > current_min:
            continue

        if depth == N-1:
            if summation < current_min:
                current_min = summation
            continue

        for i in range(N):
            if i not in visited_col:
                stack.append([depth+1, i])

    print('#{} {}'.format(t, current_min))