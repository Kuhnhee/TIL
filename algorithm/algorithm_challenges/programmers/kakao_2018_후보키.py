
from itertools import combinations

def isUnique(relation, size, idxs):
    #idxs에 속한 column들로 key를 만들엇을 때, 후보키가 될 수 있는지를 검증
    column = []
    for i in range(size):
        temp = []
        for idx in idxs:
            temp.append(relation[i][idx])
        temp = tuple(temp)
        column.append(temp)

    return len(set(column)) == size

def solution(relation):
    size = len(relation)

    key_set = []

    column_set = set(range(0,len(relation[0])))
    for i in range(1,len(relation[0])+1):

        for case in combinations(column_set, i):
            
            case_abandon = False
            for key in key_set:
                if set(key).issubset(set(case)):
                    case_abandon = True
                    break
            if case_abandon:
                continue

            if isUnique(relation, size, case):
                key_set.append(case)

    answer = len(key_set)
    return answer

if __name__ == "__main__":
    # a = set([1,2,3])
    # print(len(a))
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    solution(relation)