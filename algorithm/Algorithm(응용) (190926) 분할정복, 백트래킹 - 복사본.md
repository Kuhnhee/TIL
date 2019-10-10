# SSAFY Algorithm (190926)

## 분할정복

**설계 전략**

- 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
- 통합(Combine) : (필요하다면) 해결된 해답을 모은다.
- **Top-down approach**



### 병합 정렬(Merge Sort)

여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

**시간 복잡도**

- `O(nlogn)`



### 퀵 정렬(Quick Sort)

**병합 정렬과의 차이**

1. 기준 아이템(**pivot item**)을 중심으로 두 부분으로 나눈다.
2. 부분 정렬이 끝난 후, **"병합"**이란 후처리 작업이 **필요하지 않다**.

**알고리즘**

```pseudocode
quicksort(A[], l, r)
	if l < r
		s = partition(a, l, r)
		quicksort(A[], l, s-1)
		quicksort(A[], s+1, r)
```

**Hoare-Partition**

```pseudocode
partition(A[], l, r)
	p = A[l]
	i=l, j=r
	WHILE i <= j
		WHILE A[i] <= p : i++
		WHILE A[j] >= p : j++
		IF i < j : swap(A[i], a[j])
	
	swap(A[l], A[j])
	RETURN j
```

**Lomuto Partition**

```pseudocode
partition(A[], p, r)
	x = A[r]
	i = p-1
	FOR j in p -> r-1
		IF A[j] <= x
			i++, swap(A[i], A[j])
			
	swap(A[i+1], A[r])
	RETURN i+1
```



### 이진 검색(Binary Search)

자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

이진 검색을 하기 위해서는 자료가 **정렬된 상태**여야 한다.

**검색 과정**

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 차을 때까지 1~3 반복

**알고리즘(반복구조)**

```pseudocode
binarySearch(n, s[], k)
low = 0
high = n-1

WHILE low <= high AND location = 0
	mid = low + (high-low)/2
	
	IF S[mid] == key
		RETURN mid
	ELIF S[mid] > key
    	high = mid-1
    ELSE
    	low = mid+1
RETURN -1
```

**알고리즘(재귀구조)**

```pseudocode
binarySearch(S[], low, high, key)
	IF low > high
		RETURN -1
	ELSE
		mid = (low+high)/2
		IF key == S[mid]
			RETURN mid
		ELIF key < a[mid]
			RETURN binarySearch(a[], low, mid-1, key)
		ELSE
			RETURN binarySearch(a[], mid+1, high, key)
```





## 백트래킹

대표적 문제: N-Queen 문제

1. 상태 공간 트리의 DFS 실시
2. 각 노드가 유망한지를 검사
3. 유망하지 않다면, 그 노드의 부모 노드로 돌아가서 검색을 계속 (가지치기,**pruning** : 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다.)

**알고리즘**

```pseudocode
checknode(node v)
	IF promising(v)
		IF there is a solution at v
			wrtie the solution
		ELSE
			FOR each child u of v
				checknode(u)
```

**{1,2,3}의 powerset을 구하는 백트래킹 알고리즘**

```pseudocode
backtrack(a[], k, input)
	c[MAXCANDIDATES]
	ncands
	
	IF k == input : process_solution(a[], k)
	ELSE
		k++
		make_candidates(a[], k, input, c[], ncands)
		FOR i IN 0 -> ncands-1
			a[k] = c[i]
			backtrack(a, k, input)
main()
	a[MAX] //powerset을 저장할 배열
	backtrack(a[], 0, 3) //3개의 원소를 가지는 powerset
```

```pseudocode
make_candidates(a[], k, n, c[], ncands)
	c[0] <- True
	c[1] <- False
	ncands <- 2
	
process_solution(a[], k)
	FOR i IN 1 -> k
		IF a[i] == TRUE : print(i)
```

**백트래킹을 이용하여 순열 구하기**

```pseudocode
backtrack(a[], k, input)
	c[MAXCANDIDATES]
	ncands
	
	IF k == input : process_solution(a[], k)
	ELSE
		k++
		make_candidates(a[], k, input, c[], ncands)
		FOR i IN 0 -> ncands-1
			a[k] = c[i]
			backtrack(a, k, input)
main()
	a[MAX] //powerset을 저장할 배열
	backtrack(a[], 0, 3) //3개의 원소를 가지는 powerset
```

```pseudocode
make_candidates(a[], k, n, c[], ncands)
	in_perm[NMAX] <- FALSE
	
	FOR i IN 1 -> k-1
		in_perm[a[i]] <- TRUE
		
	ncand = 0
	FOR i IN 1 -> n
		IF in_perm[i] == FALSE
			c[ncands] <- i
			ncands++
process_solution(a[], k)
	FOR i IN 1 -> k : print(a[i])
```



