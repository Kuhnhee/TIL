
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())


for t in range(1, T+1):
    N = int(input())
    field = []

    for n in range(N):
        row = [int(i) for i in input()]
        field.append(row)

        for idx,num in enumerate(row):
            if num == 3:
                end = [n, idx]
            elif num == 2:
                start = [n, idx]

    #BFS
    answer = 0
    q = [ [start[0],start[1],0] ]
    while q:
        pos = q[0]
        q = q[1:]

        if field[pos[0]][pos[1]] == 3:
            answer = pos[2]-1
            break

        field[pos[0]][pos[1]] = 1

        for i in range(4):
            target = [pos[0]+dr[i], pos[1]+dc[i]]

            if not (0<=target[0]<N and 0<=target[1]<N):
                continue

            elif field[target[0]][target[1]] == 1:
                continue

            else:
                q.append([target[0],target[1],pos[2]+1])

    print('#{} {}'.format(t,answer))
            
