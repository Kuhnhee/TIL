def solution(N, stages):
    reach_cnt = [0 for _ in range(N)]
    unclear_cnt = [0 for _ in range(N)]
    success_rate = [0 for _ in range(N)]

    for num in stages:

        if num == N+1:
            num = N
        else:
            unclear_cnt[num-1] += 1
        for i in range(num):
            reach_cnt[i] += 1

    for i in range(N):
        if reach_cnt[i] == 0:
            success_rate[i] = [ i+1, 0 ]
            continue
        success_rate[i] = [ i+1, unclear_cnt[i]/reach_cnt[i] ]

    success_rate.sort(key=lambda x:(x[1]), reverse=True)
    answer = [s[0] for s in success_rate]
    return answer

if __name__ == "__main__":
    solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]	)