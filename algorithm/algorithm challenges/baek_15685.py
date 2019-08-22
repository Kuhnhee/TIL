def rotate(coord):
    rot = [[0,-1],[1,0]] #90 degrees clockwise (좌상단이 0,0인 경우)
    new_x = rot[0][0]*coord[0] + rot[0][1]*coord[1]
    new_y = rot[1][0]*coord[0] + rot[1][1]*coord[1]
    return [new_x, new_y]

def drawDragon(curve):
    x, y, d, g = map(int, curve)
    dx,dy = [1, 0, -1, 0], [0, -1, 0, 1] #우 상 좌 하
    path = [[x,y], [x+dx[d],y+dy[d]]] #generation 0

    while g > 0:
        end = path[-1]
        delta_x = -end[0] if end[0]>=0 else end[0]
        delta_y = -end[1] if end[1]>=0 else end[1]

        new_coord_list = []
        for coord in path:
            new_coord = rotate([coord[0]+delta_x, coord[1]+delta_y])
            new_coord_list.append([new_coord[0]-delta_x, new_coord[1]-delta_y])
        path += new_coord_list[::-1][1:]

        g-=1
    return path


N = int(input())
field =[ [0 for _ in range(101)] for _ in range(101) ]
curves = []
for n in range(N):
    curves.append(list(map(int,input().split())))   #x, y, d, g

for curve in curves:
    dragon = drawDragon(curve)

    for coord in dragon:
        field[coord[1]][coord[0]] = 1

cnt = 0
#box checker
for i in range(100):
    for j in range(100):
        if field[i][j] == 1:
            if field[i][j+1]==1 and field[i+1][j]==1 and field[i+1][j+1]==1:
                cnt += 1

print(cnt)