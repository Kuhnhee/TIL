from pprint import pprint

def DFS(pos, buffer):

    if len(buffer) == 7:
        results.add(buffer)
        return

    else:
        for i in range(4):
            target_r = pos[0]+dr[i]
            target_c = pos[1]+dc[i]
            if (0<=target_r<4 and 0<=target_c<4):
                DFS((target_r,target_c), buffer+str(board[target_r][target_c]))

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for t in range(1, T+1):
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))

    results = set()
    for r in range(4):
        for c in range(4):
            DFS((r,c), str(board[r][c]))

    print('#{} {}'.format(t, len(results)))