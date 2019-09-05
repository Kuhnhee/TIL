'''
길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
단계 2로 돌아간다.

'''
from pprint import pprint

def solution(msg):
    db = {}
    for num in range(1,27):
        db[chr(65+num-1)] = num
    code = 27

    buffer = ''
    printed = []
    for c in msg:

        buffer += c

        if buffer not in db:
            printed.append(db[buffer[:-1]])
            db[buffer] = code
            code += 1
            buffer = c
    
    printed.append(db[buffer])


    # pprint(db)
    # print(printed)

    answer = printed
    return answer

if __name__ == "__main__":

    msgs = ["KAKAO", "TOBEORNOTTOBEORTOBEORNOT", "ABABABABABABABAB"]

    for msg in msgs:
        solution(msg)