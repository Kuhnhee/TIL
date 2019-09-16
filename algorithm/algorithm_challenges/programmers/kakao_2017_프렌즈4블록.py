
def delete(m, n, board, deleted_flag, cnt):

    deleted_flag = False
    deleted = []
    for r in range(m-1):
        for c in range(n-1):
            #check 2x2
            current = board[r][c]
            if current != 0 and current == board[r+1][c] == board[r][c+1] == board[r+1][c+1]:
                dr = [r, r+1, r, r+1]
                dc = [c, c, c+1, c+1]
                for i in range(4):
                    if [dr[i], dc[i]] not in deleted:
                        deleted_flag = True
                        deleted.append([dr[i], dc[i]])

    for coord in deleted:
        board[coord[0]][coord[1]] = 0
        cnt+=1
        
    if deleted_flag:
        #push from top
        for col in range(n):
            #for each column, push to bottom
            zeros, temp = [], []
            for row in range(m):
                if board[row][col] == 0:
                    zeros.append(0)
                else:
                    temp.append(board[row][col])

            temp = zeros + temp
            #update board
            for row in range(m):
                board[row][col] = temp[row]

    return board, deleted_flag, cnt


def solution(m, n, board):

    #initialize board to 2d array
    field = []
    for row in board:
        field.append([c for c in row])
    board = field

    cnt = 0
    deleted_flag = True
    while deleted_flag:
        board, deleted_flag, cnt = delete(m, n, board, deleted_flag, cnt)

    answer = cnt
    return answer