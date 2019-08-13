
'''
  0
3   1 
  2

dir = 0 ~ 3
왼쪽 회전: (dir - 1)%4
후진: (dir+2)%4
'''
from pprint import pprint

def rotate(field, N, M, r, c, d):
    going_back = False
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    cnt = 0
    notFound = True
    while notFound and cnt!=4:
        d = (d-1)%4
        cnt += 1
        t_r = r + dr[d]
        t_c = c + dc[d]

        if 0<=t_r<N and 0<=t_c<M and field[t_r][t_c] != 1 and field[t_r][t_c] != 2:
            notFound = False
            break

    if notFound and cnt==4:
        #후진
        d = (d+2)%4
        t_r = r + dr[d]
        t_c = c + dc[d]
        if 0<=t_r<N and 0<=t_c<M and field[t_r][t_c] != 1:
            going_back = True
            return d, going_back
        else:
            return -1, going_back

    return d, going_back

N, M = map(int, input().split())
r, c, d = map(int, input().split())
field = []
for n in range(N):
    row = list(map(int,input().split()))
    field.append(row)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cleaned = 0
moving = True
while moving:
    #clean
    if field[r][c] != 2:
        field[r][c] = 2
        cleaned+=1
    
    d, going_back = rotate(field, N, M, r, c, d)
    if d == -1:
        break

    r = r + dr[d]
    c = c + dc[d]

    #recover direction(후진)
    if going_back:
        d = (d+2)%4

print(cleaned)

