T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    idx = 0
    start = data[0]
    for k in range(K):
        if idx+M == N:
            idx = N
        else:
            idx = (idx+M)%(N)
        data.insert(idx,0)
        N += 1
        if idx-1 >= 0:
            data[idx] += data[idx-1]
        if idx+1 < N:
            data[idx] += data[idx+1]
        else:
            data[idx] += start
    
    answer = data[-10:][::-1]
    print('#{} {}'.format(t, ' '.join(map(str,answer))))