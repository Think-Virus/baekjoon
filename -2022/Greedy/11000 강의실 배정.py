# Si에 시작해서 Ti에 끝나는 N개의 수업
# 최소의 강의실을 사용해서 모든 수업을 가능하게
# 수업이 끝난 직후에 다음 수업을 시작할 수 있다

# 처음 수업이 끝나고 바로 다음으로 오는 수업 찾기

# N이 최대 20만이기 때문에 O(n^2)의 시간 복잡도로는 무조건 time over 걸림
# -> 정렬을 잘 사용해서 해결 필요

# 해결 알고리즘 확인 : https://hongcoding.tistory.com/79
# 1. 현재 회의실에서의 회의가 끝나는 시간보다 다음 회의의 시작시간이 빠르면 회의실을 하나 추가로 개설한다.
# 2. 현재 회의실에서 회의가 끝나는 시간보다 다음 회의의 시작시간이 느리면 현재 존재하는 회의실에서 이어서 회의 개최가 가능하다.

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
class_list = []
class_room = []

for _ in range(N) :
    class_list.append(tuple(map(int,sys.stdin.readline().rstrip().split()))) # 회의의 [시작, 끝] 시간을 세트로 하나의 리스트에 모두 입력

class_list.sort() # 시작시간을 기준으로 정렬

heapq.heappush(class_room,class_list[0][1]) # 첫 회의의 종료시간을 새로운 큐에 넣어줌

# 이제 2번째 회의부터 첫 회의와 비교
# 두 번째 회의의 시작 시간이 첫 회의의 종료시간보다 빠르면 새로 회의를 개최
# 아니면 기존 회실 확인

# 아래 코드는 room에서 한 번 pop을 해주고 새로운 회의 시간을 push하는 것 -> 새로 회의를 개설해야 하면, room에서 개로운 회의의 종료시간을 push해주면 됨
# 우선순위 큐를 쓰는 이유? -> 종료시간이 빠른 회의부터 다음 회의를 이어서 개최해야 하기 때문
for _class in class_list[1:] :
    end_time = heapq.heappop(class_room)
    if end_time > _class[0] : # 새로운 회의 개설
        heapq.heappush(class_room,_class[1])
    else :
        end_time = _class[1]
    heapq.heappush(class_room,end_time)

print(len(class_room))