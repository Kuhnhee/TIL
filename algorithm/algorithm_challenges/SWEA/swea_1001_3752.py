
T = int(input())
for t in range(1, T+1):
    N = int(input())
    problems = list(map(int,input().split()))
    sums = set([0])
 
    for p_val in problems:
        sums_list = list(sums)
        for sum_val in sums_list: sums.add(sum_val+p_val) 

    print('#{} {}'.format(t, len(sums)))



# def DFS(num):
#     global score, result

#     if not visited[score]:
#         result += 1
#         visited[score] = 1

#     if num == N:
#         return

#     for i in range(2):
#         if i == 0:
#             #take score
#             score += problems[num] 
#             DFS(num+1)
#             score -= problems[num]
#         else:
#             #dont take score
#             DFS(num+1)

# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     problems = list(map(int, input().split()))
#     result = 0
#     visited = [0]*(sum(problems)+1)
#     score = 0
#     DFS(0)

#     print('#{} {}'.format(t, sum(visited)))


################################################################


'''
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
'''




'''
T = int(input())
for tc in range(T):
    print('#{} '.format(tc+1), end='')
    n = int(input())
    li = list(map(int, input().split()))
    m = sum(li) + 1
    visited = [0] * m
    visited[0] = 1
    score = 0
 
    for i in range(n):
        t = []
        for j in range(m):
            if visited[j]:
                t.append(li[i]+j)
 
        for tt in t:
            visited[tt] = 1
 
    # print(visited)
    print(sum(visited))
'''