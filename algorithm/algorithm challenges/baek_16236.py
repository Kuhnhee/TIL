'''
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만,
 그 물고기가 있는 칸은 지나갈 수 있다.


'''
from collections import deque

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

field = []
fishes = []
shark_size, shark_ate, fish_cnt = 2, 0, 0
N = int(input())
for n in range(N):
    row = list(map(int, input().split()))
    field.append(row)
    for idx,area in enumerate(row):
        if area == 9:
            shark = [n, idx]
        elif area != 0:
            fishes.append([n,idx,area,True])
            fish_cnt += 1

time = 0
while True:

    edible = list(filter(lambda x: x[2] < shark_size, fishes))
    if len(edible) == 0:
        break

    #calc distances for edibles(BFS), find next location of shark
    visited, candidates = [], []
    q = deque([ [shark[0], shark[1], 0] ])
    break_signal, break_depth = False, 0
    while q:
        pos = q.popleft()

        if break_signal and pos[2] != break_depth:
            break

        for fish in edible:
            if (fish[3]==True) and (fish[:2]==pos[:2]):
                candidates.append(fish)
                break_signal, break_depth = True, pos[2]
                break
        if break_signal:
            continue

        for i in range(4):
            target = [pos[0]+dr[i], pos[1]+dc[i]]
            if (not (0<=target[0]<N and 0<=target[1]<N)) or (field[target[0]][target[1]] > shark_size) or (target in visited):
                continue
            else:
                q.append([target[0], target[1], pos[2]+1])
                visited.append(target)

    # if no candidates were found, break the loop
    if not candidates:
        break

    #search among current depth(pos[2]), find prior edible fish
    target = candidates[0]
    for fish in candidates[1:]:
        if fish[0] < target[0]:
            target = fish
        elif fish[0] == target[0] and fish[1] < target[1]:
            target = fish

    #move, grow
    fish_cnt -= 1
    shark_ate += 1
    if shark_ate == shark_size:
        shark_size += 1
        shark_ate = 0
    time += break_depth
    fishes.remove(target)
    field[shark[0]][shark[1]] = 0
    shark = [target[0], target[1]]
    field[shark[0]][shark[1]] = 9

print(time)