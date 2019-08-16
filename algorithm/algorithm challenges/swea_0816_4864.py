T = int(input())
for t in range(1, T+1):
    N = input()
    M = input()

    exist = False
    l_n, l_m = len(N), len(M)

    for i in range(l_m-l_n+1):
        if M[i:i+l_n] == N:
            exist = True

    answer = 1 if exist else 0
    print('#{} {}'.format(t, answer))