'''
https://www.acmicpc.net/problem/15686

도시의 칸은 (r, c)와 같은 형태로 나타내고 r과 c는 1부터 시작한다.
도시의 각 칸은 빈 칸, 치킨집, 집 

치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

0은 빈 칸, 1은 집, 2는 치킨집이다.

치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
'''
import itertools

N, M = map(int, input().split())

field, houses, chickens = [], [], []
for n in range(N):
    row = list(map(int,input().split()))
    field.append(row)

    for idx, num in enumerate(row):
        if num == 1:
            houses.append([n, idx])
        elif num == 2: 
            chickens.append([n, idx])
        else:
            pass

current_min = 100000
for i in range(1, M+1):
    for case in itertools.combinations(chickens, i):
        current_sum = 0
        for house in houses:
            chick_dist = 100000
            for chicken in case:
                dist = abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])
                if dist < chick_dist:
                    chick_dist = dist

            current_sum += chick_dist

        if current_sum < current_min:
            current_min = current_sum

print(current_min)