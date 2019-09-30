def DFS(num):
    global answer, current_summation

    if num == N:
        if current_summation < answer:
            answer = current_summation
        return

    if current_summation > answer:
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            current_summation += board[num][i]
            DFS(num+1)
            visited.pop()
            current_summation -= board[num][i]

T = int(input())

for t in range(1, T+1):
    N = int(input())

    answer = 10000000
    current_summation = 0
    visited = []
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    DFS(0)

    print('#{} {}'.format(t, answer))