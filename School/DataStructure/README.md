# Data Structure

- [Arrays and Lists](#Arrays-and-Lists)
  - Arrays
  - Singly Linked Lists
  - Doubly Linked Lists
- [Queue and Stacks](#Queue-and-Stacks)
  - Queues
  - Stacks
- [Heaps and Priority queues](#Heaps-and-Priority-queues)
  - Priority queues
  - Heaps
- [Hash, Skip Lists and Sets](#Hash,-Skip-Lists-and-Sets)
  - Hash
  - Skip Lists
  - Sets
- [Trees](#Trees)
- [Search Trees](#Search-Trees)
  - Binary Search Trees
  - AVL Trees
  - 2,4 Trees
  - Red-Black Trees
- [Sorting](#Sorting ) (추후 Algorithm 파트로 이동)
  - Merge-Sort
  - Quick-Sort
  - Bucket-Sort
  - Radix-Sort
- [Graphs](#Graphs)
  - Graphs
  - Graph Traversal: DFS, BFS
  - DAG and topological sorting
  - Shortest Paths
    - Dijkstra's Algorithm
  - Minimum Spanning Trees
    - Prim-Jarnik's Algorithm
    - Kruskal's Algorithm





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

SLL을 순회하여 원하는 값을 찾을 경우, head node에서부터 순차적으로 탐색해야 한다. 이는 `O(n)`에 가능하다. 이는 삽입&삭제 과정에서도 마찬가지이다. Array와 시간 복잡도는 동일하지만, 향후 Tree 구조에서 Linked List를 활용할 수 있다.

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



## Hash, Skip Lists and Sets



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
- h $\le$ i  





## Search Trees



## Sorting



## Graphs

