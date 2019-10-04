# # 정사각형 방
# def DFS(r, c, depth, start):
#     global answer_start, answer_length

#     #상하좌우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     # print(r, c, depth, start)
#     if depth >= answer_length:
#         if depth == answer_length and start<answer_start:
#             answer_start = start
#         elif depth > answer_length:
#             answer_length = depth
#             answer_start = start
#             # print("new answer_start:", answer_start, r, c)
#     for i in range(4):
#         tr = r + dr[i]
#         tc = c + dc[i]
#         # print(visited, "checking ", tr,tc)
#         if (0<=tr<N and 0<=tc<N) and (tr,tc) not in visited:
#             if board[tr][tc] == board[r][c] + 1:
#                 # print("check")
#                 visited[(tr,tc)] = 1
#                 DFS(tr,tc,depth+1,start)
#                 visited.pop((tr,tc))

# T = int(input())
# for t in range(1, T+1):
#     board = []
#     N = int(input())
#     for n in range(N):
#         board.append(list(map(int, input().split())))

#     answer_start = N**2 + 1
#     answer_length = 0
#     for r in range(N):
#         for c in range(N):

#             if c>=1 and board[r][c] == board[r][c-1] + 1:
#                 continue

#             visited = {}
#             visited[(r,c)]= 1
#             DFS(r, c, 1, board[r][c])


#     print('#{} {} {}'.format(t, answer_start, answer_length))


# 정사각형 방
T = int(input())
for t in range(1, T+1):
    board = []
    N = int(input())
    for n in range(N):
        board.append(list(map(int, input().split())))

    #상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    answer_start = N**2 + 1
    answer_length = 0
    for r in range(N):
        for c in range(N):

            if (c>=1 and board[r][c] == board[r][c-1]+1) or (r>=1 and board[r][c] == board[r-1][c]+1):
                continue
            if (c<N-1 and board[r][c] == board[c][c+1]+1) or (r<N-1 and board[r][c] == board[r+1][c]+1):
                continue

            stack = [ [(r,c),1,(r,c)] ]
            while stack:
                pos = stack.pop()
                # print(pos, answer_length, answer_start)
                if pos[1] > answer_length:
                    answer_length = pos[1]
                    answer_start = board[pos[2][0]][pos[2][1]]
                elif pos[1] == answer_length:
                    if answer_start > board[pos[2][0]][pos[2][1]]:
                        answer_start = board[pos[2][0]][pos[2][1]]

                for i in range(4):
                    tr = pos[0][0] + dr[i]
                    tc = pos[0][1] + dc[i]

                    if (0<=tr<N and 0<=tc<N):
                        if board[tr][tc] == board[pos[0][0]][pos[0][1]] + 1:
                            stack.append([(tr,tc), pos[1]+1, pos[2]])

    print('#{} {} {}'.format(t, answer_start, answer_length))


'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''