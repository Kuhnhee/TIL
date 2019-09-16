class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    heads, tails = [], []
    for m in range(M):
        line = list(map(int, input().split()))
        
        head = Node(line[0])
        former_node = head
        for num in line[1:]:
            new_node = Node(num)
            former_node.next = new_node
            former_node = new_node
        heads.append(head)
        tails.append(new_node)

    base = heads[0]
    for i in range(1, M):
        compare = heads[i]

        former_node = base
        current_node = base
        found_flag = False
        while current_node != None:
            if current_node.data > compare.data:
                if current_node == base:
                    found_flag = True
                    tails[i].next = current_node
                    base = compare
                else:
                    found_flag = True
                    tails[i].next = current_node
                    former_node.next = compare
                break

            former_node = current_node
            current_node = current_node.next

        if not found_flag:
            former_node.next = compare


    answer = []
    head = base
    current_node = head
    while current_node != None :
        answer.append(current_node.data)
        current_node = current_node.next

    answer = answer[-10:][::-1]
    print('#{} {}'.format(t, ' '.join(map(str, answer))))