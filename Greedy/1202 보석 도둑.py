# 내가 잘못 생각했던 부분은 jewel에 넣은 항목을 heaqp.heappop으로 빼오면서 삭제하면 비교가 안될 거라고 생가했는데 아래처럼 구현하면 됨
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
bag = []
for _ in range(N):
    heapq.heappush(jewel, list(map(int, input().split())))
for _ in range(K):
    bag.append(int(input()))

bag.sort() # 가방의 크기가 작은 순으로 정렬

result = 0
candidate = []
for b in bag:
    while jewel and b >= jewel[0][0]: # 작은 순으로 하고 그냥 넣어버리는 이유가 어차피 다음에 대입될 가방의 크기는 현재보다 크기 때문에 보석을 넣을 수 있음
        w, v = heapq.heappop(jewel)
        heapq.heappush(candidate, -v) # 최대 힙을 구현하기 위해 -를 붙임

    if candidate:
        result -= heapq.heappop(candidate) # 들어갈 수 있는 보석 중 가장 큰 값을 가져옴

print(result)