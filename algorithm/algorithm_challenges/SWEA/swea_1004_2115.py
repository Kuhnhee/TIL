# 벌꿀채취
from pprint import pprint

def local_dfs(board, arr, idx, summation, base_summation):
    global maximum

    if idx == len(arr):
        if summation > maximum:
            maximum = summation
        return
    else:
        for i in range(2):
            if i == 0:
                if base_summation+arr[idx] > C:
                    continue
                local_dfs(board, arr, idx+1, summation+arr[idx]**2, base_summation+arr[idx])
            else:
                local_dfs(board, arr, idx+1, summation, base_summation)


T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())

    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    current_max = 0
    memo = {}
    for r in range(N):
        for c in range(N-M+1):
            maximum = 0
            local_dfs(board, board[r][c:c+M], 0, 0, 0)
            memo[(r,c)] = maximum

    for r in range(N):
        for c in range(N-M+1):
            value1 = memo[(r,c)]

            value2 = 0
            for c2 in range(c+M, N-M+1):
                value2 = memo[(r,c2)]
                if value1 + value2 > current_max:
                    current_max = value1 + value2
            for r2 in range(r+1,N):
                for c2 in range(N-M+1):
                    value2 = memo[(r2,c2)]
                    if value1 + value2 > current_max:
                        current_max = value1 + value2
                        
    print('#{} {}'.format(t, current_max))



'''
10
4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
3 3 10
7 2 9
6 6 6
5 5 7
4 1 10
8 1 8 2
4 6 1 6
4 9 6 3
7 4 1 3
4 3 12
8 8 6 5
5 2 7 4
8 5 1 7
7 8 9 4
5 2 11
7 5 9 9 6
7 3 7 9 3
1 7 1 4 5
1 7 9 2 6
6 6 8 3 8
6 3 20
8 5 2 4 3 1
4 3 6 1 1 8
4 4 1 2 3 1
1 7 4 9 6 1
6 5 1 2 8 4
3 1 4 5 1 3
7 2 11
2 8 2 5 2 8 6
2 3 7 4 6 4 8
3 7 8 3 9 4 4
8 8 5 9 3 6 9
9 7 6 2 4 1 3
2 9 2 8 9 7 3
2 1 7 2 7 8 3
8 3 12
9 1 6 7 5 4 6 7
9 5 1 8 8 3 5 8
5 2 6 8 6 9 2 1
9 2 1 8 7 5 2 3
6 5 5 1 4 5 7 2
1 7 1 8 1 9 5 5
6 2 2 9 2 5 1 4
7 1 1 2 5 9 5 7
9 4 20
5 2 4 8 3 7 6 2 1
7 9 8 5 8 2 6 3 6
1 9 4 6 7 5 3 1 1
4 4 7 6 2 2 8 1 7
9 6 8 5 7 3 7 9 5
7 3 1 4 1 1 8 5 3
4 6 8 9 4 5 3 8 8
1 3 4 2 4 1 1 3 6
5 9 2 3 5 2 4 8 5
10 5 30
7 4 7 5 9 3 6 4 6 7
8 9 8 4 5 7 8 9 2 9
6 5 3 4 6 4 7 6 3 2
4 7 4 3 4 7 3 3 4 3
3 5 6 4 8 8 2 1 8 6
3 7 9 7 1 7 6 2 8 9
3 6 1 6 8 9 7 7 5 1
4 3 5 6 2 1 2 6 3 6
3 4 9 2 1 5 9 9 6 3
9 9 7 3 7 5 5 5 8 4

'''