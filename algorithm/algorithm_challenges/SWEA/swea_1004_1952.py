# 수영장

T = int(input())
for t in range(1, T+1):
    d, m, tm, y = map(int, input().split())
    plans = list(map(int, input().split()))

    memo = [0]*12
    plans = plans[::-1]
    for idx,p in enumerate(plans):

        if idx==0:
            memo[11-idx] = min(d*p, m, tm, y)
            continue
        
        #1일치: d*p / 한달: m / 세달: tm / 년:y
        if_day = memo[11-idx+1]+d*p
        if_month = memo[11-idx+1]+m
        if 11-idx+3 < 12:
            if_three_month = memo[11-idx+3]+tm
        else:
            if_three_month = tm
        if_year = y

        memo[11-idx] = min(if_day, if_month, if_three_month, if_year)

    print('#{} {}'.format(t, memo[0]))

'''
10
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
10 70 180 400
6 9 7 7 7 5 5 0 0 0 0 0
10 70 200 550
0 0 0 0 8 9 6 9 6 9 8 6
10 80 200 550
0 8 9 15 1 13 2 4 9 0 0 0
10 130 360 1200
0 0 0 15 14 11 15 13 12 15 10 15
10 180 520 1900
0 18 16 16 19 19 18 18 15 16 17 16
10 100 200 1060
12 9 11 13 11 8 6 12 8 7 15 6
10 170 500 1980
19 18 18 17 15 19 19 16 19 15 17 18
10 200 580 2320
12 28 24 24 29 25 23 26 26 28 27 22
'''