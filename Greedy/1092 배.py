# 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다!
# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성


"""
원래 로직 반례
3
6 8 9
9
1 2 3 4 5 6 7 8 9
-> 내림차순으로 도전
"""
import sys
import heapq

N = int(sys.stdin.readline())
Crane_list = list(map(int, sys.stdin.readline().split()))

def Box_minus(val) :
    return int(val)*-1

M = int(sys.stdin.readline())
Box_list = list(map(Box_minus, sys.stdin.readline().split()))

while True :
    if max(Crane_list) < min(Box_list) :
        anser = -1
        break

    # 오름차순 정렬
    Crane_list.sort(reverse=True)
    heapq.heapify(Box_list) # -값으로 오름차순됨

    # 동시에 움직일 수 있는 것 체크해야 함!
    # 틀린 이유로 추측되는 거는 가장 센 애로만 들 수 있는 애가 있는 거야 그러면 못드는 게 맞을듯.
    var_repeat = True
    anser = 0
    tmp_list = []
    while True:
        Box_list = Box_list + tmp_list
        if not Box_list :
            break
        heapq.heapify(Box_list)
        tmp_list = []
        for Crane in Crane_list :
            if not Box_list :
                break
            Box = heapq.heappop(Box_list)
            while True :
                if Crane < -1*Box and Box_list :
                    tmp_list.append(Box)
                    Box = heapq.heappop(Box_list)
                else:
                    break
        anser += 1

    print(anser)
    break
