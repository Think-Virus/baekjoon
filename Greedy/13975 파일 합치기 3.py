# 소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다.
# 소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다.
# 이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 파일을 합쳐나가고,
# 최종적으로는 하나의 파일로 합친다. 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

# 예를 들어, C1, C2, C3, C4가 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자.
# 이 파일들을 합치는 과정에서, 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 이때 비용 60이 필요하다.
# 그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다.
# 최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다.
# 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 다른 방법으로 파일을 합치면 비용을 줄일 수 있다.
# 먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다.
# 이때 필요한 총 비용은 70+80+150=300 이다.
"""
heapq 사용하면 될듯
"""
import heapq
import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    K = int(sys.stdin.readline())
    size_heap = list(map(int,sys.stdin.readline().split()))
    heapq.heapify(size_heap)

    cost = 0
    while len(size_heap) >= 2 :
        mixed_size = heapq.heappop(size_heap) + heapq.heappop(size_heap)
        cost += mixed_size
        heapq.heappush(size_heap,mixed_size)
    print(cost)


