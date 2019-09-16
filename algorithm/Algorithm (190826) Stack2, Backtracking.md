# SSAFY Algorithm (190826)

## Stack2

- 중위표기법(infix)
- 후위표기법(postfix) -> Stack 이용하여 연산



### 백트래킹

- 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.
- 백트래킹 기법은 **최적화 문제**와 **결정 문제**를 해결할 수 있다.
- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes'또는 'no'가 답하는 문제
  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합(Subset Sum) 문제 등

#### 백트래킹과 깊이우선탐색의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 (Prunning 가지치기)
- 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- 깊이우선탐색을 가하기에는 경우의 수가 너무 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 DFS를 가하면 당연히 처리 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(exponential time)을 요하므로 처리 불가능



#### 연습문제

{1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합 구하기

```python
def backtrack(k, sum):
    global cnt
    cnt+=1
    if k==N:
        if sum==0:
            for i in range(1,11):
                if a[i] == True:
                    print(i,end=' ')
            print()
    else:
        k += 1
        a[k] = 1; backtrack(k, sum+k)
        a[k] = 0; backtrack(k, sum)
N = 10
a = [0]*(N+1)
cnt = 0
backtrack(0,0)

#cnt = 2047

#backtrack 수정버전
def backtrack(k, sum):
    global cnt
    cnt+=1
    if k==N:
        if sum==10:
            for i in range(1,11):
                if a[i] == True:
                    print(i,end=' ')
            print()
    else:
        k += 1
		if sum + k<= 10:
            a[k] = 1; backrack(k, sum+k)
        a[k] = 0; backtrack(k, sum)
        
N = 10
a = [0]*(N+1)
cnt = 0
backtrack(0,0)

# cnt = 250

```



### 분할 정복

#### 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
- 병합정렬과의 차이: 
  1. 기준 아이템 (pivot)을 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다. 
  2. 각 부분 정렬이 끝난 후, 합병정렬은 "합병"이란 후처리 작업이 필요하나, 퀵정렬은 필요로 하지 않는다.

