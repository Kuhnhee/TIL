from pprint import pprint

r, c, k = map(int, input().split())
r -= 1
c -= 1

field = []
for i in range(3):
    field.append(list(map(int, input().split())))

time = 0
while True:
    R = len(field)
    C = len(field[0])

    if time > 100:
        answer = -1
        break

    if R>r and C>c:
        if field[r][c] == k:
            answer = time
            break

    flip_flag = False
    if R >= C:
        pass
    else:
        field = [list(elem) for elem in zip(*field)][::-1]
        flip_flag = True

    longest = 0
    for idx,row in enumerate(field):

        row = [num for num in row if num != 0]
        rowset = set(row)

        datas = []
        for elem in rowset:
            datas.append([elem, row.count(elem)])

        #정렬
        datas.sort(key=lambda x:(x[1], x[0]))
        new_row = []
        for data in datas:
            new_row += data

        if len(new_row) > 100:
            new_row = new_row[:100]

        field[idx] = new_row

        if len(new_row) > longest:
            longest = len(new_row)


    for idx,row in enumerate(field):
        if len(row) < longest:
            for concat in range(longest-len(row)):
                field[idx]+=[0]

    if flip_flag:
        field = [list(elem) for elem in zip(*field[::-1])]

    time += 1

print(answer)