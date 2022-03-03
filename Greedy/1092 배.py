# 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다!
# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성
import sys
from collections import deque

N = int(sys.stdin.readline())
Crane_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Box_list = list(map(int, sys.stdin.readline().split()))

while True :
    if max(Crane_list) < min(Box_list) :
        anser = -1
        break

    # 오름차순 정렬
    # Crane_list = deque(sorted(Crane_list))
    # Box_list = deque(sorted(Box_list))
    Crane_list = (sorted(Crane_list))
    Box_list = (sorted(Box_list))
    # 동시에 움직일 수 있는 것 체크해야 함!

    anser = 0
    var_continue = True
    if N < M:  # 작은 걸 기준으로 확인하는 게 빠를 것이라고 판단함
        while Box_list and var_continue:
            for Crane in Crane_list:
                #if Crane < Box_list.popleft():
                if not Box_list :
                    break
                if Crane < Box_list.pop(0):
                    var_continue = False
                    break
            anser += 1
    else:
        while Crane_list and var_continue:
            for Box in Box_list:
                if not Box_list :
                    break
                #if Box < Crane_list.popleft():
                if Box < Crane_list.pop(0):
                    var_continue = False
                    break
            anser += 1
    break
print(anser)