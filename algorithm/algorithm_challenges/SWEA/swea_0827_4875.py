T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    start, end = [], []
    field = []
    for n in range(N):
        row = input()
        row_list =[]
        for idx,c in enumerate(row):
            row_list.append(int(c))
            if c == '2':
                start = [n, idx]
            elif c == '3':
                end = [n, idx]
        field.append(row_list)
        
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    pos = start
    stack = [pos]
    while stack:
        pos = stack.pop()
        field[pos[0]][pos[1]] = 1

        for i in range(4):
            target_pos = [pos[0]+dr[i],pos[1]+dc[i]]

            if not (0<=target_pos[0]<N and 0<=target_pos[1]<N):
                continue

            if field[target_pos[0]][target_pos[1]] == 1:
                continue
            else:
                stack.append(target_pos)
    
    if field[end[0]][end[1]] == 1:
        answer = 1
    else:
        answer = 0
    print('#{} {}'.format(t, answer))




