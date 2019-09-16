T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    datas = list(map(int,input().split()))
    for m in range(M):
        idx, data = map(int, input().split())
        datas.insert(idx, data)
    print('#{} {}'.format(t, datas[L]))