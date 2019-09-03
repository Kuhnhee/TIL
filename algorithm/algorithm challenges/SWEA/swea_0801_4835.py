T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    current_max = 0
    current_min = 0
    for m in range(M):
        current_max += data[m]
        current_min += data[m]

    for n in range(1,N-M+1):
        current_sum = 0
        for m in range(M):
            current_sum += data[n+m]
        
        if current_sum > current_max:
            current_max = current_sum
        
        if current_sum < current_min:
            current_min = current_sum
        
    # print(f'{current_max} {current_min}')
    print('#{0} {1}'.format(t, current_max-current_min))