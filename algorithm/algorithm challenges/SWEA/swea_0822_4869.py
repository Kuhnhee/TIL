T = int(input())
def calc(pos, N):
    if pos == N:
        return 1
    elif pos > N:
        return 0
    else:
        return calc(pos+10, N) + calc(pos+20, N)*2

for t in range(1,T+1):
    N = int(input())
    answer = calc(0, N)
    print('#{} {}'.format(t, answer))