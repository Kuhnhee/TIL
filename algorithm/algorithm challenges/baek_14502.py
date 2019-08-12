'''
https://www.acmicpc.net/problem/14502

새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

'''
import itertools

'''
상하좌우
dx(행) = [-1,1,0,0]
dy(열) = [0,0,1,-1]
'''
def run(field, empty_coords, virus_coords, comb, current_max):
    N = len(field)
    M = len(field[0])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    safe_area = len(empty_coords)
    virus_num = len(virus_coords)
    
    for wall in comb:
        field[wall[0]][wall[1]] = 1
    safe_area -= 3

    breakflag = False
    changed = True
    while changed:
        changed = False

        for virus in virus_coords:

            for direc in range(4):
                target_x = virus[0] + dx[direc]
                target_y = virus[1] + dy[direc]

                if 0<=target_x<N and 0<=target_y<M and field[target_x][target_y] != 2:
                    if field[target_x][target_y] != 1:
                        safe_area -= 1
                        field[target_x][target_y] = 2
                        virus_coords.append([target_x,target_y])
                        changed = True
                        if safe_area < current_max:
                            breakflag=True
                            break
            if breakflag:
                break

    new_viruses = virus_coords[virus_num:]
    #recover field
    for wall in comb:
        field[wall[0]][wall[1]] = 0
    for virus in new_viruses:
        field[virus[0]][virus[1]] = 0

    #recover virus_coords
    virus_coords = virus_coords[:virus_num]

    return safe_area, virus_coords

N, M = map(int, input().split())
field = []
empty_coords = []
virus_coords = []
for n in range(N):
    row = list(map(int,input().split()))
    for idx,num in enumerate(row):
        if num == 0:
            empty_coords.append([n,idx])
        elif num == 2:
            virus_coords.append([n,idx])
    field.append(row)

current_max = 0
for comb in itertools.combinations(empty_coords, 3):

    safe_area, virus_coords = run(field, empty_coords, virus_coords, comb, current_max)
    if safe_area > current_max:
        current_max = safe_area
    
print(current_max)
