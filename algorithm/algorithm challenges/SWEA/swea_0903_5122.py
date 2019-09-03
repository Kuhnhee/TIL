T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    datas = list(map(int, input().split()))
    for m in range(M):
        line = input().split()

        if line[0] == 'I':
            datas.insert(int(line[1]), int(line[2]))

        elif line[0] == 'D':
            datas.pop(int(line[1]))

        elif line[0] == 'C':
            datas[int(line[1])] = int(line[2])

    if len(datas) <= L:
        answer = -1
    else:
        answer = datas[L]

    print('#{} {}'.format(t, answer))
