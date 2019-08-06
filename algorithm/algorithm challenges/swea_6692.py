T = int(input())

for t in range(1,T+1):
    N = int(input())

    summation = 0
    for n in range(N):
        p, x = map(float, input().split())
        summation += p*x
    
    print('#{} {}'.format(t, summation))