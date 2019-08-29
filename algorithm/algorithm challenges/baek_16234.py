'''
국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
'''
from pprint import pprint

N, L, R = map(int, input().split())

field = []
for n in range(N):
    field.append(list(map(int, input().split())))

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
moved = True
while moved:
    moved = False
    allies = []
    for i in range(N):
        for j in range(N):

            if field[i][j] > 0:
                population = 0
                stack = [[i,j]]
                ally, memorize, recover = [], [], []
                while stack:
                    pos = stack.pop()
                    population += field[pos[0]][pos[1]]
                    memorize = field[pos[0]][pos[1]]
                    recover.append([pos[0], pos[1], memorize])
                    field[pos[0]][pos[1]] = 0
                    ally.append(pos)

                    for d in range(4):
                        target_pos = [pos[0]+dr[d], pos[1]+dc[d]]

                        if not (0<=target_pos[0]<N and 0<=target_pos[1]<N):
                            continue

                        if field[target_pos[0]][target_pos[1]] == 0 or target_pos in stack:
                            continue

                        if L<=abs(memorize-field[target_pos[0]][target_pos[1]])<=R:
                            stack.append(target_pos)
                            moved=True

                num = len(ally)
                ally.append(population//num)
                allies.append(ally)

                #recover
                if not moved:
                    for coord in recover:
                        field[coord[0]][coord[1]] = coord[2]

    if moved:
        for ally in allies:
            pop = ally[-1]
            for coord in ally[:-1]:
                field[coord[0]][coord[1]] = pop
        cnt+=1
print(cnt)

    