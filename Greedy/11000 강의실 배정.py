# Si에 시작해서 Ti에 끝나는 N개의 수업
# 최소의 강의실을 사용해서 모든 수업을 가능하게
# 수업이 끝난 직후에 다음 수업을 시작할 수 있다

# 처음 수업이 끝나고 바로 다음으로 오는 수업 찾기

"""
8
1 3
1 5
2 4
2 5
3 4
3 5
5 9
7 8
"""

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
class_list = []
class_room = 0

for _ in range(N) :
    heapq.heappush(class_list,tuple(map(int,sys.stdin.readline().rstrip().split())))

while len(class_list) - 1 :
    class_room += 1
    spare_list = []
    start_class = heapq.heappop(class_list)
    for _ in range(len(class_list)) :
        _class = heapq.heappop(class_list)
        if start_class[1] > _class[0] :
            heapq.heappush(spare_list,_class)
        else :
            start_class = _class
    if spare_list :
        class_list = spare_list

if class_list :
    class_room += 1

print(class_room)