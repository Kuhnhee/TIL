def solution(dartResult):
    bonus = 'SDT'
    option = '*#'

    # 1. parsing
    chances = []
    buffer = ''
    for c in dartResult:
        if c.isdigit():
            if buffer != '' and not buffer[-1].isdigit():
                chances.append(buffer)
                buffer = ''
            buffer += c
        elif c in bonus:
            buffer += c
        else:
            buffer += c
    chances.append(buffer)

    # 2. calculate points (basic points, bonuses)
    score = [0, 0, 0]
    options = ['', '', '']
    for idx, val in enumerate(chances):
        buffer = ''
        for c in val:
            if c.isdigit():
                buffer+=c
            elif c in bonus:
                bo = c
            elif c in option:
                op = c
                options[idx] = op
        score[idx] += int(buffer)
        if bo == 'D':
            score[idx] = score[idx]**2
        elif bo == 'T':
            score[idx] = score[idx]**3
        
        
    print(score, options)
    # 3. calculate option effects
    for idx, val in enumerate(options):
        if val == '*':
            score[idx] *= 2
            if idx-1 >=0:
                score[idx-1] *= 2
        elif val == '#':
            score[idx] *= -1
            
    answer = sum(score)
    return answer

if __name__ == "__main__":
    solution('1D#2S*3S')