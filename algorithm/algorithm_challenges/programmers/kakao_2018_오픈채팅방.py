'''
db = {
    uid1234 : {
        nick : "Prodo"
        act : [ ... , act, act2, ...]
    }
}

'''
from collections import deque

def solution(record):
    db = {}
    query_ids = [] #행위를 한 id 순서 (Change는 저장 안함)
    for query in record:

        query = query.split()
        if len(query) == 3:
            command, identify, nick = query
        else:
            command, identify = query
        
        if identify not in db:
            db[identify] = {
                'nick' : None,
                'act' : deque([])
            }

        if command == 'Enter':
            db[identify]['act'].append(command)
            db[identify]['nick'] = nick
            query_ids.append(identify)
            
        elif command == 'Leave':
            db[identify]['act'].append(command)
            query_ids.append(identify)

        elif command == 'Change':
            db[identify]['nick'] = nick

    answer = []
    for identify in query_ids:

        nick = db[identify]['nick']
        command = db[identify]['act'].popleft()

        if command == 'Enter':
            action = '들어왔습니다.'
        elif command == 'Leave':
            action = '나갔습니다.'
        line = '{}님이 {}'.format(nick, action)
        answer.append(line)

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    solution(record)