N = int(input())

tp = []
for n in range(N):
    t, p = map(int, input().split())
    tp.append([t,p])
tp.reverse()

#memo[i] = i+1일까지 얻을 수 있는 최대 수익 저장
memo = [0]*N

#초기조건
if tp[0][0] == 1:
    memo[0] = tp[0][1]

for i in range(1,N) :
    #ending_day = 현재 상담의 예상 종료일
    ending_day = tp[i][0] + (N-i)

    #현재 상담을 택했을 때, 더 이상 다른 상담을 받지 못할 경우.
    if ending_day == N+1:
        memo[i] = max(memo[i-1], tp[i][1])
    #현재 상담을 택했을 때, 예상 종료일이 퇴사일이거나 그 이전일 경우.
    elif ending_day <= N:
        memo[i] = max(memo[i-1], tp[i][1]+memo[N-ending_day])
    #현재 상담의 예상 종료일이 퇴사일 이후인 경우(착수 불가)
    else:
        memo[i] = memo[i-1]

print(memo[-1])