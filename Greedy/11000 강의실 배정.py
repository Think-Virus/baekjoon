# Si에 시작해서 Ti에 끝나는 N개의 수업
# 최소의 강의실을 사용해서 모든 수업을 가능하게
# 수업이 끝난 직후에 다음 수업을 시작할 수 있다

# 처음 수업이 끝나고 바로 다음으로 오는 수업 찾기

import sys
N = int(sys.stdin.readline().rstrip())
class_list = []
class_room = 0

for _ in range(N) :
    class_list.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

class_list.sort(key= lambda x:(x[0],x[1]))

while len(class_list) - 1 > 0  :
    class_room += 1
    class_0 = class_list[0]
    class_list = class_list[1:]
    for _class in class_list :
        if class_0[1] <= _class[0] : # 0의 위치의 수업의 끝보다 0다음의 수업의 시작이 큰 경우
            class_list.remove(_class)
            class_0 = _class

if len(class_list) :
    class_room += 1

print(class_room)