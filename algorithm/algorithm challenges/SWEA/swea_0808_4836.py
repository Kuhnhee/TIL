# SWEA 4836 색칠하기

T = int(input())
for t in range(1,T+1):

    field = [[0 for _ in range(10)] for _ in range(10)]

    N = int(input())
    mix_cnt = 0 
    for n in range(N):
        row = list(map(int, input().split()))
        left_top = row[0:2]
        right_bot = row[2:4]
        color = row[4]
        width = right_bot[1] - left_top[1] +1
        height = right_bot[0] - left_top[0] +1

        for i in range(height):
            for j in range(width):
                if field[left_top[0]+i][left_top[1]+j] == 0:
                    field[left_top[0]+i][left_top[1]+j] = color
                elif field[left_top[0]+i][left_top[1]+j] == 3: #mixed area
                    pass
                else:
                    field[left_top[0]+i][left_top[1]+j] = 3 #mix
                    mix_cnt += 1
                
    answer = mix_cnt
    print('#{} {}'.format(t,answer))