'''
낚시왕
https://www.acmicpc.net/problem/17143
'''

'''
  상 하 우 좌
d=[1, 2, 3, 4]
'''
from pprint import pprint

def move(R, C, shark):
    # shark = [r, c, s, d, z]
    power = shark[2]

    if shark[3] == 1 or shark[3] == 2:
        for i in range(power % (2*(R-1))):
            if shark[3] == 1:
                if shark[0] == 0:
                    shark[3] = 2
                    shark[0] += 1
                else:
                    shark[0] -= 1
            else:
                if shark[0] == R-1:
                    shark[3] = 1
                    shark[0] -= 1
                else:
                    shark[0] += 1

    elif shark[3] == 3 or shark[3] == 4:
        for i in range(power % (2*(C-1))):
            if shark[3] == 3:
                if shark[1] == C-1:
                    shark[3] = 4
                    shark[1] -= 1
                else:
                    shark[1] += 1
            else:
                if shark[1] == 0:
                    shark[3] = 3
                    shark[1] += 1
                else:
                    shark[1] -= 1

    return shark


R, C, M = map(int, input().split())

field =[[[] for _ in range(C)] for _ in range(R)]

sharks = []
for m in range(M):
    r, c, s, d, z = map(int, input().split())
    field[r-1][c-1] = [[r-1, c-1, s, d, z]]
    sharks.append([r-1, c-1, s, d, z])

cnt = 0
pos = -1
while pos+1 < C:

    # 낚시왕 이동
    pos += 1
    # 낚시왕 사냥
    for i in range(R):

        if field[i][pos] != []:
            cnt += field[i][pos][0][4]
            sharks.remove(field[i][pos][0])
            field[i][pos] = []
            break
    # 상어 이동
    for shark in sharks:
        field[shark[0]][shark[1]].remove(shark)
        shark = move(R, C, shark)
        field[shark[0]][shark[1]].append(shark)

    sharks = []
    for r in range(R):
        for c in range(C):
            if field[r][c] != []:
                
                if len(field[r][c])>=2:
                    field[r][c].sort(key=lambda x:x[4], reverse=True)
                    field[r][c] = [field[r][c][0]]
                sharks.append(field[r][c][0])

print(cnt)