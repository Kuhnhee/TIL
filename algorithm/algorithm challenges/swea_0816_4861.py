def isPelindrom(word):
    return word == word[::-1]

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    field = []
    for n in range(N):
        field.append(input())

    answer = ''
    col_buffers = ['']*N
    getout = False
    for i in range(N):
        row_buffer = field[i][:M]
        if isPelindrom(row_buffer):
            answer = row_buffer
            break

        for j in range(N):

            if 0<=i<M:
                col_buffers[j] += field[i][j]
                if len(col_buffers[j]) == M:
                    if isPelindrom(col_buffers[j]):
                        answer = col_buffers[j]
                        getout = True
                        break

            #update buffers
            elif i<=N-1:
                col_buffers[j] = col_buffers[j][1:] + field[i][j]
                if len(col_buffers[j]) == M:
                    if isPelindrom(col_buffers[j]):
                        answer = col_buffers[j]
                        getout = True
                        break
            
            if j>=M:
                row_buffer = row_buffer[1:] + field[i][j] 
                if isPelindrom(row_buffer):
                    answer = row_buffer
                    break

        if getout:
            break

    print('#{} {}'.format(t, answer))