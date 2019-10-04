# 창용 마을 무리의 개수

from pprint import pprint

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    phoneBook = {}
    for m in range(M):
        p1, p2 = map(int, input().split())

        if p1 in phoneBook:
            phoneBook[p1].append(p2)
        else:
            phoneBook[p1] = [p2]

        if p2 in phoneBook:
            phoneBook[p2].append(p1)
        else:
            phoneBook[p2] = [p1]

    answer = 0
    group_found = {}
    for person in range(1, N+1):
        if person in group_found:
            continue
        
        stack = [person]
        while stack:
            current_num = stack.pop()
            group_found[current_num] = 1
            if current_num not in phoneBook:
                continue
            else:
                nums = phoneBook[current_num]

            for num in nums:
                if num not in group_found and num not in stack:
                    stack.append(num)
        answer += 1
    
    print('#{} {}'.format(t, answer))
'''
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''