for t in range(1,11):
    t_num = int(input())
    row_stack = []
    for _ in range(100):
        row = input()
        row_stack.append(row)

    col_stack = [[row_stack[i][j] for i in range(100)] for j in range(100)]

    max_length = 1
    for l in range(2, 101):
        searchNextL = False
        if l-max_length>2:
            break
        for j in range(101-l):
            for i in range(100):
                row_buffer = row_stack[i][j:j+l]
                col_buffer = col_stack[i][j:j+l]

                if row_buffer == row_buffer[::-1] or col_buffer == col_buffer[::-1]:
                    max_length = l
                    searchNextL = True
                    break
            if searchNextL:
                break

    print('#{} {}'.format(t, max_length))
