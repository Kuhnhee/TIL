def solution(answers):

    corrects = {
        1: 0,
        2: 0,
        3: 0,
    }

    #1번: [1,2,3,4,5] 반복
    #2번: [2,1,2,3,2,4,2,5] 반복
    #3번: [3,3,1,1,2,2,4,4,5,5] 반복
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for idx,ans in enumerate(answers):

        #1번 정답인가?
        if one[idx%5] == ans:
            corrects[1]+=1 

        #2번 정답인가?
        if two[idx%8] == ans:
            corrects[2]+=1

        #3번 정답인가?
        if three[idx%10] == ans:
            corrects[3]+=1

    
    # corrects 중 가장 큰 값을 가진 번호 찾기
    temp, answer = [], []
    maxval = 0
    for key, val in corrects.items():
        temp.append([key,val])
        if val > maxval:
            maxval = val

    temp.sort(key=lambda x:(x[1], x[0]))
    for candidate in temp:
        if candidate[1] == maxval:
            answer.append(candidate[0])

    print(answer)
    return answer