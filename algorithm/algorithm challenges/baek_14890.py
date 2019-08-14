'''
https://www.acmicpc.net/problem/14890
을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.
'''

def linechecker(line, N, L):
    flag = True
    former_val = line[0]
    buffer = [line[0]]

    for idx, num in enumerate(line):
        if idx == 0:
            continue
        if abs(num)==abs(former_val):
            if num+former_val == 0:
                buffer=[]
            buffer.append(num)

        else:
            #차이가 2 이상인지 확인
            if abs(num - abs(former_val))>1:
                flag = False
                break

            # 좌측(혹은 우측) 여유공간 있는지 확인
            if num == abs(former_val)+1:

                # idx, num 기준 좌측 L개 칸 확인
                if L>len(buffer) or former_val<0:
                    flag = False
                    break
                else:
                    #initialize buffer
                    buffer = [num]

            else:   #우측
                # dix, num 기준 우측 L-1개 칸 확인
                if N-idx < L:
                    flag = False
                    break
                else:
                    # 우측 L-1개 칸의 검증
                    temp_former = num
                    temp_buffer = [idx]
                    for l in range(1,L):
                        if temp_former != line[idx+l]:
                            flag = False
                            break
                        else:
                            temp_former = line[idx+l]
                            temp_buffer.append(idx+l)
                    else:
                        for temp in temp_buffer:
                            line[temp] *= -1
                    #initialize buffer
                    buffer = []
                    
                    if flag == False:
                        break
        former_val = line[idx]
            
    return flag


if __name__ == "__main__":

    N, L = map(int, input().split())
    row_check = [True]*N
    col_check = [True]*N
    col_stack = [[]]*N
    row_stack = []

    for n in range(N):
        row = list(map(int,input().split()))
        row_stack.append(row)

    col_stack = [*map(list, zip(*row_stack))]

    cnt = 0
    for row in row_stack:
        if linechecker(row, N, L):
            cnt += 1
    
    for col in col_stack:
        if linechecker(col, N, L):
            cnt += 1


    print(cnt)

