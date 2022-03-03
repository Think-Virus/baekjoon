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
    Crane_list = (sorted(Crane_list))
    Box_list = deque(sorted(Box_list))
    # 동시에 움직일 수 있는 것 체크해야 함!
    # 틀린 이유로 추측되는 거는 가장 센 애로만 들 수 있는 애가 있는 거야 그러면 못드는 게 맞을듯.

    anser = 0
    var_continue = True
    while Box_list and var_continue:
        for Crane in Crane_list:
            Box = Box_list.popleft()
            if not Box_list :
                break
            if Crane < Box:
                Box_list.appendleft(Box)
        anser += 1
    print(anser)
    break