import itertools

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())

viruses = []
empty = 0
field = []
for n in range(N):
    row = list(map(int, input().split()))
    field.append(row)

    for idx, num in enumerate(row):
        if num == 2:
            viruses.append([n, idx])
        if num == 0:
            empty += 1

backup = empty

answer = 100000
for case in itertools.combinations(viruses, M):
    
    empty = backup
    recover = []
    q = []
    for coord in case:
        q.append(coord+[0])

    break_signal = False
    while q:
        pos = q.pop(0)

        for i in range(4):
            target = [pos[0]+dr[i], pos[1]+dc[i]]

            if (not (0<=target[0]<N and 0<=target[1]<N)) or (field[target[0]][target[1]] == 1):
                continue
            
            elif field[target[0]][target[1]] == 0:
                q.append([target[0], target[1], pos[2]+1])
                empty -= 1
                recover.append(target)
                field[target[0]][target[1]] = 1
            
            elif field[target[0]][target[1]] == 2:
                q.append([target[0], target[1], pos[2]+1])
                field[target[0]][target[1]] = 1

            if empty == 0:
                break_signal = True
                break

        if break_signal:
            break

    if break_signal:
        time = q[-1][2]
        if time < answer:
            answer = time

    #recover
    for coord in recover:
        field[coord[0]][coord[1]] = 0
    for coord in viruses:
        field[coord[0]][coord[1]] = 2
    empty = backup

if answer == 100000:
    answer = -1

if empty == 0:
    answer = 0

print(answer)