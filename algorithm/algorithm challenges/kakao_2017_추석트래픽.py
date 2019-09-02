'''
모든 시간을 초로 환산한 풀이
'''

def solution(lines):
    datas = []
    for line in lines:
        parsed = line.split()
        end, time = parsed[1], float(parsed[2][:-1])
        
        hour, minute, sec = map(float, [end[:2], end[3:5], end[6:]])

        end = hour*3600 + minute*60 + sec
        start = round(end-time+0.001, 3)
        if start<0:
            start = 0

        datas.append([start, end])

    N = len(datas)
    current_max = 0
    for idx,data in enumerate(datas):

        starting = data[1] #각 로그의 끝 지점들을 검색 시작점으로 선택

        ending = round(starting + 1 - 0.001, 3)

        cnt = 0
        for i in range(idx, N):
            target = datas[i]

            if starting<=target[0]<=ending or starting<=target[1]<=ending or (target[0]<starting and target[1]>ending):
                cnt += 1

        if cnt>current_max:
            current_max=cnt

    answer = current_max
    return answer

if __name__ == "__main__":
    lines = ["2016-09-15 23:59:59.999 0.1s"]
    answer = solution(lines)
    print(answer)
