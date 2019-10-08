def solution(heights):
    answer = []

    heights = [[idx+1, h] for idx, h in enumerate(heights)]

    heights = heights[::-1]

    while heights:
        current = heights.pop(0)
        for tower in heights:
            if tower[1] > current[1]:
                answer.append(tower[0])
                break
        else:
            answer.append(0)


    answer.reverse()
    return answer