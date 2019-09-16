from pprint import pprint

def solution(board):

    #상하좌우
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]

    N = len(board)

    shapes = {}

    # BFS to find blocks
    for r in range(N):
        for c in range(N):
            if board[r][c] != 0 and board[r][c] not in shapes:
                num = board[r][c]
                shapes[num] = []
                q=[[r,c]]
                while q:
                    pos = q.pop(0)
                    shapes[num].append(pos)

                    for i in range(4):
                        target = [pos[0]+dr[i], pos[1]+dc[i]]
                        if not (0<=target[0]<N and 0<=target[1]<N):
                            continue
                        if board[target[0]][target[1]] != num:
                            continue
                        if target in q or target in shapes[num]:
                            continue
                        q.append(target)

    impossible_list = []
    #더이상 직사각형을 만들 수 없는 블록이 발견되지 않을 때까지 반복문 시행
    found = True
    while found:
        found=False
        for key,val in shapes.items():

            # 현재 블록이 점유해야 할 2x3 혹은 3x2 직사각형의 좌상단, 우하단 좌표를 찾는다.
            max_c, min_c = 0, 200
            max_r, min_r = 0, 200
            for coord in val:
                if coord[0] > max_r:
                    max_r = coord[0]
                if coord[0] < min_r:
                    min_r = coord[0]

                if coord[1] > max_c:
                    max_c = coord[1]
                if coord[1] < min_c:
                    min_c = coord[1]

            abandon_block = False
            for r in range(min_r,max_r+1):
                for c in range(min_c, max_c+1):

                    # 자기 자신에 의해 가로막혀서 직사각형을 만들 수 없는 경우
                    if board[r][c] != key and r>min_r:
                        for temp in range(1,r-min_r+1):
                            if board[r-temp][c] == key:
                                impossible_list.append(key)
                                abandon_block = True
                                found = True
                                break
                    if abandon_block:
                        break

                    # 직사각형을 만들 수없는 블록에 의해 가려진 경우
                    if board[r][c] != key:
                        for temp in range(0, min_r+1):
                            if board[r-temp][c] != 0 and board[r-temp][c] in impossible_list:
                                impossible_list.append(key)
                                abandon_block = True
                                found = True
                                break
                if abandon_block:
                    break

        # 직사각형을 만드는 것이 불가능한 블록들을 shapes에서 삭제
        for key in impossible_list:
            if key in shapes:
                shapes.pop(key)
        
    answer = len(shapes)
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
    solution(board)