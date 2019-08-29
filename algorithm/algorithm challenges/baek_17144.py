'''
미세먼지 안녕!
https://www.acmicpc.net/problem/17144
'''

# 상 우 하 좌
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

R, C, T = map(int, input().split())

field, machine, dusts = [], [], []
for r in range(R):
    row = list(map(int, input().split()))
    field.append(row)
    for idx,num in enumerate(row):
        if num >= 5:
            dusts.append([r, idx, num])
        if num == -1:
            machine.append([r, 0])
top, bottom = machine

while T>0:
    #확산
    for dust in dusts:
        row, col, dval = dust
        spreading_cnt = 0
        val = dval//5
        for i in range(4):
            target = [row+dr[i], col+dc[i]]
            if (not (0<=target[0]<R and 0<=target[1]<C)) or (field[target[0]][target[1]] == -1):
                continue
            field[target[0]][target[1]] += val
            spreading_cnt += 1
        field[row][col] -= val*spreading_cnt

    #회전
    #상단(반시계) row: 0, top[0]  / col: 0, C-1
    for r in range(top[0]-1, 0, -1):
        field[r][0] = field[r-1][0]
    for c in range(C-1):
        field[0][c] = field[0][c+1]
    for r in range(top[0]):
        field[r][C-1] = field[r+1][C-1]
    for c in range(C-1, 1, -1):
        field[top[0]][c] = field[top[0]][c-1]
    field[top[0]][1] = 0

    #하단(시계) row: bottom[0], R-1  / col: 0, C-1
    for r in range(bottom[0]+1, R-1):
        field[r][0] = field[r+1][0]
    for c in range(C-1):
        field[R-1][c] = field[R-1][c+1]
    for r in range(R-1, bottom[0], -1):
        field[r][C-1] = field[r-1][C-1]
    for c in range(C-1, 1, -1):
        field[bottom[0]][c] = field[bottom[0]][c-1]
    field[bottom[0]][1] = 0

    dusts = []
    for r in range(R):
        for c in range(C):
            if field[r][c] >= 5:
                dusts.append([r,c,field[r][c]])
    T -= 1

total = 0
for row in field:
    total += sum(row)
print(total+2)
