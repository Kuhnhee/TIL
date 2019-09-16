from collections import deque

'''
wheel = [N, NE, E, SE, S, SW, W, NW]
왼쪽=wheel[6] / 오른쪽=wheel[2]
시계방향 회전 -> wheel.rotate(1)
반시계방향 회전 -> wheel.rotate(-1)
'''
whls = []
for _ in range(4):
    wheel = deque(input())
    whls.append(wheel)

K = int(input())
rotates = []
for k in range(K):
    num, clock = map(int, input().split())
    rotates.append([num, clock])

for rot in rotates:
    num, clock = rot[0]-1, rot[1]

    corresponding_rotates = [[num,clock]]
    #왼쪽 변경범위 체크
    former_num = num
    for i in range(1,num+1):
        temp_clock = -clock if i%2!=0 else clock

        current_whl_idx = num-i
        if whls[former_num][6] != whls[current_whl_idx][2]:
            corresponding_rotates.append([current_whl_idx, temp_clock])
            former_num = current_whl_idx
        else:
            break

    #우측 변경범위 체크
    former_num = num
    for i in range(1,4-num):
        temp_clock = -clock if i%2!=0 else clock

        current_whl_idx = num+i
        if whls[former_num][2] != whls[current_whl_idx][6]:
            corresponding_rotates.append([current_whl_idx, temp_clock])
            former_num = current_whl_idx
        else:
            break

    # whls[num].rotate(clock)
    for corr in corresponding_rotates:
        whls[corr[0]].rotate(corr[1])

#score calc
score = 0
for idx,wheel in enumerate(whls):
    score += int(wheel[0])*(2**(idx))
print(score)