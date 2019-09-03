from pprint import pprint


for t in range(1,11):
    field = []
    t_num = int(input())

    starts = []
    first = list(map(int, input().split()))
    for i in range(100):
        if first[i] == 1:
            starts.append([0,i])

    field.append(first)
    for i in range(99):
        row = list(map(int,input().split()))
        field.append(row)

    for pos in starts:
        answer = pos[1]
        for i in range(99):
            #go down
            pos[0] += 1

            l_r =[-1, 1]
            left_right = -1
            #좌우 check
            if pos[1]-1>=0 and field[pos[0]][pos[1]-1]==1:
                left_right = 0
            elif pos[1]+1<=99 and field[pos[0]][pos[1]+1]==1:
                left_right = 1
            else:
                pass
            
            if left_right != -1:
                while True:
                    temp = pos[1]+l_r[left_right]
                    if 0<=temp<100 and field[pos[0]][temp]!=0:
                        pos[1] = temp
                    else:
                        break

        if field[pos[0]][pos[1]] == 2:
            break
    
    print('#{} {}'.format(t_num,answer))