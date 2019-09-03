'''
https://www.acmicpc.net/problem/14889

축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

'''
import itertools

#DFS로 팀 분할
def DFS(people, depth=0, team1=[], team2=[]):
    l = len(people)/2

    if len(team1) == l and len(team2) == l:
        yield team1, team2

    else:
        for i in range(2):
            if i == 0:
                if len(team1) < l:
                    team1.append(people[depth])
                    yield from DFS(people, depth+1, team1, team2)
                    team1.pop()
            else:
                if len(team2) < l:
                    team2.append(people[depth])
                    yield from DFS(people, depth+1, team1, team2)
                    team2.pop()
        
N = int(input())
n = N/2
S = []
for n in range(N):
    row = list(map(int,input().split()))
    S.append(row)

people = list(range(N))

current_min = 1000000
for team1, team2 in DFS(people):
    team1_score = 0
    team2_score = 0
    for perm in itertools.permutations(team1,2):
        team1_score += S[perm[0]][perm[1]]
    for perm in itertools.permutations(team2,2):
        team2_score += S[perm[0]][perm[1]]

    diff = abs(team1_score-team2_score)

    if diff < current_min:
        current_min = diff

print(current_min)