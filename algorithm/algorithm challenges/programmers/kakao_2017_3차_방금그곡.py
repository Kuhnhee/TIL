def parser(music):
    sound_parsed = []
    buffer = ''
    for s in music:
        if buffer != '' and s != '#':
            sound_parsed.append(buffer)
            buffer = ''
        buffer += s
    sound_parsed.append(buffer)
    return sound_parsed

def solution(m, musicinfos):

    m_parsed = parser(m)

    candidates = []
    for music in musicinfos:
        start, end, title, sound = music.split(',')
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])

        # sound parsing
        sound_parsed = parser(sound)


        idx = 0
        played = []
        time = end - start
        for t in range(time):
            played.append(sound_parsed[idx])
            idx = (idx+1)%len(sound_parsed)


        # 패턴이 존재하는가?
        for i in range(time-len(m_parsed)+1):
            if played[i:i+len(m_parsed)] == m_parsed:
                candidates.append([time, title])
                break

    #select among candidates
    if not candidates:
        return '(None)'
    answer = candidates[0]
    for music in candidates:
        if music[0] > answer[0]:
            answer = music

    # print(answer[1])
    return answer[1]

if __name__ == "__main__":
    solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
    # solution("ABCDEFG", ["13:00,13:05,WORLD,ABCDEF","12:00,12:14,HELLO,CDEFGAB"])
    # solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
    solution("ABCDEFG", ["12:00,12:14,SongA,CDEFGAB", "13:00,13:14,SongB,CDEFGAB" ])