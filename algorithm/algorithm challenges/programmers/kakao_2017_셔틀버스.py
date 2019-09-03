def solution(n, t, m, timetable):

    #크루들 도착시간 
    arrivals = []
    for time in timetable:
        hour = int(time[:2])
        minute = int(time[3:])
        arrivals.append(60*hour + minute)
    arrivals.sort()

    #bustime check / 9시 = 60*9 / 간격 = t
    base = 60*9
    bustime = [base]
    bustime_dict = {base:[]}
    for i in range(1,n):
        bustime.append(base+i*t)
        bustime_dict[base+i*t] = []

    #마지막 버스 이후 도착하는 크루들은 무시
    last_time = bustime[-1]
    arrivals = list(filter(lambda x: x<=last_time, arrivals))
    
    #버스 시간별 현재 배정 인원 체크
    stack = []
    for crew in arrivals:
        for bus in bustime:
            if crew<=bus and len(bustime_dict[bus])<m:
                bustime_dict[bus].append(crew)
                break

    #탑승 가능한 가장 늦은 시간 확인
    target = None
    for bus in bustime[::-1]:
        stack = bustime_dict[bus]
        if len(stack) < m:
            target = bus    #널널하므로, 이 버스의 출발 정각에 탑승 가능
            break
        else:
            for idx,t in enumerate(stack[::-1]):
                for i in range(2):
                    #try t, t-1
                    if len(list(filter(lambda x:x<=t-i, stack))) < m:
                        target = t-i
                        break
                if target!=None:
                    break
        if target!=None:
            break

    # print(target)
    hour = str(target//60)
    minute = str(target%60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    # print(hour+':'+minute)
    return hour+':'+minute
