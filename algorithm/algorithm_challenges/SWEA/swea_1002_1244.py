# 최대 상금
def swap(string, idx1, idx2):
    tempList = list(string)
    tempList[idx1], tempList[idx2] = tempList[idx2], tempList[idx1]
    return ''.join(tempList)

def DFS(nums, depth, pos):
    global answer

    if depth == cnt:
        answer = max(nums, answer)
    else:
        #choose place to swap
        for i in range(pos, N-1):
            for j in range(i+1,N):
                if nums[i] <= nums[j]:
                    DFS(swap(nums, i, j), depth+1, i)

T = int(input())
for t in range(1, T+1):
    nums, cnt = map(str, input().split())
    cnt = int(cnt)
    N = len(nums)
    answer = nums

    DFS(nums, 0, 0) #string, depth, swapping position

    print('#{} {}'.format(t, answer))

'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
'''


# def solve(x, s):
#     global ans

#     if s:
#         for i in range(720):
#             if not state[s][i]:
#                 state[s][i] = x
#                 break
#             elif state[s][i] == x:
#                 return

#     if s == 0:
#         if x > ans: ans = x
#     else:
#         xx = list(str(x))
#         for i in range(len(xx) - 1):
#             for j in range(i + 1, len(xx)):
#                 xx[i], xx[j] = xx[j], xx[i]
#                 solve(int(''.join(xx)), s - 1)
#                 xx[i], xx[j] = xx[j], xx[i]


# for tc in range(1, int(input()) + 1):
#     x, s = map(int, input().split())

#     state = [[0] * 720 for i in range(11)]
#     ans = 0
#     solve(x, s)
#     print("#%d" % (tc), ans)