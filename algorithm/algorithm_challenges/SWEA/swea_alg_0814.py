# code = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# testcase = int(input())
# for tc in range(1, testcase+1):
#    n = input(); s = input(); ans = ''
#    for i in range(len(code)): ans += (code[i] + ' ')*s.count(code[i])
#    print("#%d\n%s" %(tc,ans))


names = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
hashmap = [[0 for _ in range(100)] for _ in range(100)]
# hashmap[ord('Z')][ord('R')] = 0
# hashmap[ord('O')][ord('N')] = 1
# hashmap[ord('T')][ord('W')] = 2
# hashmap[ord('T')][ord('H')] = 3
# hashmap[ord('F')][ord('O')] = 4
# hashmap[ord('F')][ord('I')] = 5
# hashmap[ord('S')][ord('I')] = 6
# hashmap[ord('S')][ord('V')] = 7
# hashmap[ord('E')][ord('G')] = 8
# hashmap[ord('N')][ord('I')] = 9
hashmap[90][82] = 0
hashmap[79][78] = 1
hashmap[84][87] = 2
hashmap[84][72] = 3
hashmap[70][79] = 4
hashmap[70][73] = 5
hashmap[83][73] = 6
hashmap[83][86] = 7
hashmap[69][71] = 8
hashmap[78][73] = 9
 

T = int(input())
for t in range(1, T+1):
    t_num, n = input().split()
    target = input().split()
    cnts = [0,0,0,0,0,0,0,0,0,0]
    result = ''
    for idx in range(int(n)):
        cnts[hashmap[ord(target[idx][0])][ord(target[idx][1])]] += 1
    for i in range(len(cnts)):
        result += (names[i]+' ')*cnts[i]
    print('{}\n{}'.format(t_num,result))
