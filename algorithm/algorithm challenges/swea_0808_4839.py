# SWEA 4839 이진탐색

T = int(input())
for t in range(1, T+1):
    p, a, b = map(int, input().split())
    a_l, a_r, b_l, b_r = 1, p, 1, p

    winner = 0
    gaming = True
    while gaming:
        
        a_c = int((a_l+a_r)/2)
        b_c = int((b_l+b_r)/2)

        #종료확인
        if a_c == a and b_c == b:
            winner = 0
            break
        if a_c == a:
            winner = 'A'
            break
        elif b_c == b:
            winner = 'B'
            break

        #범위변경
        if a_c > a:
            a_r = a_c
        else:
            a_l = a_c

        if b_c > b:
            b_r = b_c
        else:
            b_l = b_c
    
    print('#{} {}'.format(t, winner))