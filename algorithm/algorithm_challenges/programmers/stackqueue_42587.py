from queue import PriorityQueue

def solution(priorities, location):

    # q = PriorityQueue()
    q = [[p, idx] for idx,p in enumerate(priorities)]
    current_max = max(priorities)
    results = []

    idx = 1
    while q:
        c = q.pop(0)

        if c[0] < current_max:
            q.append(c)
        else:
            if c[1] == location:
                return idx
            else:
                current_max = max(map(lambda x:x[0], q))
            idx += 1
            


    answer = 0
    return answer

if __name__ == "__main__":

    a = solution([2, 1, 3, 2], 2)
    print(a)