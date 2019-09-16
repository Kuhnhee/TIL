T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for m in range(M):
        temp = data[0]
        data = data[1:]
        data.append(temp)

    answer = data[0]
    print('#{} {}'.format(t, answer))