# SSAFY Algorithm (190807)

## List2, 검색

- 1차월 list를 묶어놓은 list

- 행 우선 순회 / 열 우선 순회 / 지그재그 순회

  ```python
  #행 우선
  for i in range(len(Array)):
  	for j in range(len(Array[i])):
          Array[i][j]
          
  #열 우선
  for j in range(len(Array[0])):
  	for i in range(len(Array)):
          Array[i][j]
          
  #지그재그 순회
  for i in range(len(Array)):
  	for j in range(len(Array[0])):
          Array[i][j + (m-1-2*j)*(i%2)]
  ```

- 델타를 이용한 2차 배열 탐색

  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

  ```pseudocode
  arry[0.....n-1][0.....n-1]
  dx[] <- [0,0,-1,1]
  dy[] <- [-1,1,0,0]
  for x in range(len(arry)):
  	for y in range(len(arry[x])):
  		for mode in range(4):
  			textX <- x + dx[mode]
  			testY <- y + dy[mode]
  			test(arry[testX][testY])
  ```

- 전치 행렬 (대각선 기준)

  ```python
  arr = [[1,2,3],[4,5,6],[7,8,9]]
  
  for i in range(3):
      for j in range(3):
          if i<j:
              arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```

- << 연산자

  `1<<n` : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수

- & 연산자

  `i & (1<<j)`  : i의 j번째 비트가 1인지 아닌지를 리턴한다.

- 비트연산을 사용한 부분집합 생성

  ```python
  arr = [3,6,7,1,5,4]
  n = len(arr) #n=원소의 개수
  for i in range(1<<n): #1<<n = 부분 집합의 개수
      for j in range(n+1): #원소의 수만큼 비트를 비교함
          if i&(1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
              print(arr[j], end=", ")
      print()
  print()
  ```

- 응용) 합이 0이 되는 부분집합을 모두 구하라

  ```python
  arr = [3,6,7,1,5,4,-5,-9,-13,-1]
  n = len(arr) #n=원소의 개수
  for i in range(1<<n): #1<<n = 부분 집합의 개수
      summation = 0
      temp = []
      for j in range(n+1): #원소의 수만큼 비트를 비교함
          if i&(1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
              summation+=arr[j]
              temp.append(arr[j])
      if summation == 0:
          print(temp)
  ```



### 이진 검색

- 가운데 값과 비교하여 다음 검색 위치를 결정, 반복
- 이진 검색을 위해서는 반드시 자료가 정렬되어 있어야 한다.



### 셀렉션 알고리즘

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.

  최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

  1. 정렬 알고리즘을 이용하여 자료 정렬
  2. 원하는 순서에 있는 원소 가져오기



#### 선택 정렬(Selection sort)

- 자료 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
  1. 주어진 리스트 중에서 최소값을 찾는다.
  2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.



