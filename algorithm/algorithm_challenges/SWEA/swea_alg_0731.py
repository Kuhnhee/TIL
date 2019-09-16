'''
가로 길이는 항상 1000이하로 주어진다.

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)

각 빌딩의 높이는 최대 255이다.

'''
for i in range(10):
    t = int(input())
    builds = list(map(int, input().split()))
    sol = 0
    for j in range(2,t-2):
        left_higher = builds[j-1] if builds[j-1]>builds[j-2] else builds[j-2]
        right_higher = builds[j+1] if builds[j+1]>builds[j+2] else builds[j+2]
        if builds[j]>left_higher and builds[j]>right_higher:
            highest_around = left_higher if left_higher>right_higher else right_higher
        
            sol += (builds[j]-highest_around)
    print('#{0} {1}'.format(i+1, sol))
        



