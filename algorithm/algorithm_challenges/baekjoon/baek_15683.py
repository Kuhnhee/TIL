'''
5가지 cctv
회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

#1 : 4가지 [상, 하, 좌, 우]
#2 : 2가지 [상하, 좌우]
#3 : 4가지 [NE, SE, SW, NW]
#4 : 4가지 [상, 하, 좌, 우]
#5 : 1가지
사각 지대의 최소 크기를 출력한다.
'''
import itertools

def fillLine(field, free, coord, direction, recover):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while True:
        tr = coord[0] + dr[direction]
        tc = coord[1] + dc[direction]
        if tr<0 or tr>=len(field) or tc<0 or tc>=len(field[0]):
            break
        if field[tr][tc] == 6:
            break
        else:
            if field[tr][tc] == 0:
                field[tr][tc] = '#'
                free -= 1
                recover.append([tr,tc])
            coord = [tr, tc]

    return field, free, recover

N, M = map(int, input().split())
field = []
cam1, cam2, cam3, cam4, cam5 = [], [], [], [], []
free = 0
for n in range(N):
    row = list(map(int,input().split()))
    for idx, num in enumerate(row):
        if num==0:
            free += 1
        elif num==1:
            cam1.append([n,idx])
        elif num==2:
            cam2.append([n,idx])
        elif num==3:
            cam3.append([n,idx])
        elif num==4:
            cam4.append([n,idx])
        elif num==5:
            cam5.append([n,idx])
    field.append(row)

cam1_rots = itertools.product([0,1,2,3],repeat=len(cam1))
cam2_rots = itertools.product([0,1],repeat=len(cam2))
cam3_rots = itertools.product([0,1,2,3],repeat=len(cam3))
cam4_rots = itertools.product([0,1,2,3],repeat=len(cam4))

current_min = 10000000 
for case in itertools.product(cam1_rots, cam2_rots, cam3_rots, cam4_rots):
    cam1_case, cam2_case, cam3_case, cam4_case = case[0], case[1], case[2], case[3]

    #move sets for each cameras
    cam2_set = [[0,1],[2,3]]
    cam3_set = [[0,3],[3,1],[2,1],[2,0]]
    cam4_set = [[0,2,3],[0,1,3],[1,2,3],[0,1,2]]

    recover = []
    for idx, coord in enumerate(cam1):
        field, free, recover = fillLine(field, free, coord, cam1_case[idx], recover)
    
    for idx, coord in enumerate(cam2):
        for direction in cam2_set[cam2_case[idx]]:
            field, free, recover = fillLine(field, free, coord, direction, recover)

    for idx, coord in enumerate(cam3):
        for direction in cam3_set[cam3_case[idx]]:
            field, free, recover = fillLine(field, free, coord, direction, recover)

    for idx, coord in enumerate(cam4):
        for direction in cam4_set[cam4_case[idx]]:
            field, free, recover = fillLine(field, free, coord, direction, recover)

    for idx, coord in enumerate(cam5):
        for direction in range(4):
            field, free, recover = fillLine(field, free, coord, direction, recover)

    if free < current_min:
        current_min = free

    #recover
    for cover in recover:
        field[cover[0]][cover[1]] = 0
        free += 1

print(current_min)