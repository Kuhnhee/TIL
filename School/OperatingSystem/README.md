# Operating System

- [Process vs Thread](#Process-vs-Thread)
  - Multi-processing
  - Multi-Threading
- Scheduler
  - Long-term scheduler
  - Mid-term scheduler
  - Short-term scheduler
- CPU scheduler
- 프로세스 동기화
- 메모리 관리
- 가상 메모리
- 캐시 지역성





































## Process vs Thread





## Arrays and Lists

### Array

동일 타입의 변수 집합이 나열된 자료구조로, 논리적 저장 순서와 물리적 저장 순서가 일치한다. 0부터 시작되는 `index`로 원하는 `element`에의 접근이 가능하며, 정확한 인덳스 값을 알고 있는 경우 `O(1)`에 해당 원소에 접근할 수 있다.

특정 인덱스 `i`의 위치에 새로운 원소를 삽입하고 싶다면(혹은 삭제하고자 한다면), `i` 이후의 원소들을 한 칸씩 밀어내야 하므로 `O(n)`의 시간이 요구된다. 

단, Array의 끝 부분에서 원소를 삭제하거나 삽입하고자 하는 경우에는 `O(1)`에 가능하다.

- Sorted Array의 경우

  Array가 정렬되어있는 경우, **Binary Search**를 통해 `O(nlogn)`에 탐색이 가능하다.

### Linked List

선언 단계에서 크기가 정해지는 Array와 달리, Linked List는 선언 단계에서 크기가 고정되지 않는다.

#### Singly Liked List (SLL)

`head` pointer로부터 시작되는 일련의 노드들이 일방향으로 연결된 리스트 구조이다. 각각의 노드에는 `element`와 `link to next node`가 저장된다. SLL의 마지막 노드의 `link`는 `null`값을 가리킨다.

SLL을 순회하여 원하는 값을 찾을 경우, head node에서부터 순차적으로 탐색해야 한다. 이는 `O(n)`에 가능하다. 이는 삽입&삭제 과정에서도 마찬가지이다. Array와 시간 복잡도는 동일하지만, Tree 구조에서 Linked List를 활용할 수 있다.

#### Doubly Linked List (DLL)

각 노드가 `element`, `link to previous node`, `link to the next node`를 가지고 있는 구조. SLL과 달리 양방향으로 순회가 가능하다. 이로 인해 **삭제**연산이 쉬워지지만, 추가적인 공간을 요구하며 자료구조에 수정이 필요할 때 추가적인 연산을 요구한다는 단점이 있다.

#### Circular Linked List

`tail` 노드와 `head`node를 연결하여 원형으로 순회 가능한 구조. 더 이상 `head` 포인터가 필요 없으며, `tail` 포인터만 있으면 된다.



## Queues and Stacks

### Queue

`First-in First-out (FIFO)`원칙을 따르는 자료구조. 삽입(`enque`)은 queue의 맨 뒤에서 이루어지며, 삭제(`deque`)는 queue의 맨 앞에서 이루어진다. 

운영체제의 `Round-Robin Scheduler`에서 활용된다.

### Stack

`First-in Last-out (LIFO)` 원칙을 따르는 자료구조. 삽입(`push`)과 삭제(`pop`) 모두 stack의 가장 뒤(`top`)에서 이루어진다.

`JVM`의 method stack에서 활용된다.`Parentheses matching`, `HTML tag matching`, `Infix-Postfix 변환`문제에서 또한 사용된다.





## Heaps and Priority queues

### Priority queue

`entry`들의 집합을 저장하는 자료구조이다. 이 때 각각의 `entry`는 `(key, value)`쌍으로 이루어지며, key값 순서대로 값을 꺼낼 수 있다. key값은 대소관계를 비교할 수 있는 값이어야 하며, 아래와 같은 세가지 규칙을 따라야 한다.

1. Comparability property: either x $\leq$ y or y $\leq$ x
2. Antisymmetric property: x $\leq$ y and y $\leq$ x &rarr; x = y
3. Transitive property: x $\leq$ y and y $\leq$ z &rarr; x $\leq$ z

정렬되지 않은 리스트로 구현하고자 할 경우, 삽입은 맨 앞 혹은 맨 뒤에서 `O(1)`안에 이루어지며 최고 우선순위 값을 찾는 데에는 리스트 전체의 순회가 필요하므로 `O(n)`이 소요된다.

정렬된 리스트로 구현할 경우, 알맞은 위치를 찾아 삽입해야 하므로 `O(n)`이 요구되며 최고 우선수위 값은 리스트의 가장 앞 값을 참조하면 되므로 `O(1)`이 요구된다.

**Priority Queue Sorting (PQ-sort)**

Priority queue를 사용해 list를 정렬할 수 있다. list의 원소들을 한 개 씩 priority queue에 모두 삽입한 뒤, 우선순위 순서대로 priority queue에서 꺼낸다.

**Selection-sort**

priority queue가 정렬되지 않았다고 가정했을 때의 PQ-sort. Priority queue에 원소들을 삽입할 떄 O(n), 우선순위 순서대로 원소를 꺼낼 때 (1+2+3+....+n)의 시간이 걸린다. 종합적으로 O(n^2^) 시간이 걸린다.

**Insertion-sort**

priority queue가 정렬되었을 때의 PQ-sort. Priority queue에 원소들을 삽입할 떄 (1+2+3+....+n), 우선순위 순서대로 원소를 꺼낼 때 O(n)의 시간이 걸린다. 종합적으로 O(n^2^) 시간이 걸린다.

### Heap

Binary Tree 형태의 자료구조로, 각 노드의 key값으로 정렬되어 있다. 아래와 같은 성질을 만족해야 한다.

- Heap-Order: root가 아닌 모든 internal node v에 대하여, key(v) $\geq$ key(parent(v))
- Complete Binary Tree: 트리의 `height`를 h라 할 때, h-1 깊이까지 완전 이진 트리여야 한다. (i=0, ... , h-1에 대하여 깊이 i에는 2^i^ 개의 노드가 존재한다.)
- `last node`는 최대 깊이의 가장 오른쪽 노드다.

N개의 key가 저장된 heap의 `height`는 O(logN)이다.

Heap을 사용해 priority queue를 구현할 수 있다. 각각의 노드에 `(key, value)`쌍을 저장하고, 트리의 `root`가 최소 key를 가지도록 한다.

#### Insertion into a Heap

1. 새로운 `last node`의 위치 z 탐색
2. 입력값 k를 z에 저장
3. Heap-Order property recover **(Upheap)**
   - 삽입 노드로부터 부모 노드들과 값을 비교하면서, 필요하면 swap.
   - k값이 `root`에 도달하거나 Heap-Order를 만족하게 될 경우 종료
   - heap의 `height`가 `O(logn)`이므로, **upheap**에는 `O(logn)`이 소요된다.

#### Removal from a Heap

1. `root` 노드 값 삭제 &rarr; `last node ` w의 값 k를 `root`의 위치로 불러온다.
2. w 노드 삭제
3. Heap-Order property recover **(Downheap)**
   - `root`부터 시작하여 자식 노드들과 비교하면서, 필요하면 swap.
   - k값이 `leaf` 노드에 도달하거나 Heap-Order를 만족하게 될 경우 종료
   - heap의 `height`가 `O(logn)`이므로, **downheap**에는 `O(logn)`이 소요된다.

- *Array-based Heap을 구현할 경우, n번째 인덱스 값과 0번째 인덱스 값을 교환한 뒤 n번째 인덱스 값을 삭제하기만 하면 된다.*

#### Updating the Last Node

최악의 경우 `root`까지 올라갔다가 내려가야 하므로, 삽입, 삭제 모두 `O(logn)`개의 노드 순회를 필요로 한다.

#### Merging Two Heaps

두 heap 사이에 새로운 노드를 `root`로 삽입한 뒤, **downheap**과정을 통해 Heap-Order property를 만족시킨다.

#### Bottom-up Heap Construction

`n`개의 key값에 대하여, `bottom-up construction`을 통해 `logn`번의 `phase`로 heap을 구성하는 것이 가능하다. 최악의 경우, `height`가 `O(logn)`이므로 **downheap**에 의해 `O(logn)`이 소요된다고 생각할 수 있느나, heap을 구성하는 과정에서 이미 아래쪽 heap은 정렬이 완료되어 있음을 고려해야 한다. 결론적으로 n개의 노드는 각각 최대 2회만 방문되게 되므로, `bottom-up heap construction`은 `O(n)` 만을 요구한다. (`O(2n)` = `O(n)`)



## Hash, Skip Lists and Sets

### Hash

잘 정리된 [포스트](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/DataStructure#HashTable)로 대체한다.





## Trees

Tree는 Stack, Queue와 같은 선형 구조가 아닌 비선형 자료구조로, 계층적 관계를 표현한다.

**트리의 주요 키워드들**

- Root: 부모(`parent`)가 없는 노드
- Internal node: 적어도 한 개 이상의 자식(`child`)가 있는 노드
- External node (**leaf**): 자식이 없는 노드
- Ancestors: 자신보다 상위 노드 (parent, grandparent, grand-grandparent ... )
- Depth of a node: 조상(`ancestor`)의 수
- Height of a tree: 트리의 최대 깊이(`depth`)
- Descendant: 자신보다 하위 노드 (child, grandchild, grand-grandchild ... )
- Subtree: 자신을 `Root`로 삼고, 후손들을 포함하는 트리

**Preorder Traversal**

후손 노드보다 자신을 우선하여 순회하는 순회법

**Postorder Traversal**

후손 노드를 우선하여 순회하는 순회법

### Binary Tree

모든 Internal node들이 최대 2개의 자식 노드를 갖는 트리구조. `Arithmetic expression tree`, `Decision tree`, `searching(Binary search)`에 사용된다.

**키워드**

- n: 노드 수
- e: external 노드 수
- i: internal 노드 수
- h: height

**특징**

- e = i + 1
- n = 2e - 1
- h $\leq$ i
- h $\leq$ (n-1)/2
- e < 2^h^ (모든 external node가 같은 depth를 가질 때, e = 2^h)
- h >= log(e)
- h >= log(n+1) - 1

**Inorder Traversal**

이진트리에서만 가능한 순회법. 좌측 subtree를 방문한 뒤, 우측 subtree를 방문하기 전 현재 노드를 순회한다.



## Search Trees



## Sorting



## Graphs

