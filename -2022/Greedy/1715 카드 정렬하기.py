# 답 확인
# 아예 문제를 잘못 파악하고 고정관념에 박혀있었음
# 내가 착각했던 부분은 가장 작은 애들끼리 더하고 이후에는 순서대로 더하면 된다고 생각했었음
# 그러나 예를 들어서 10 50 51 52 이렇게 주어지면 내 로직대로 했을 때 답은 334이지만
# heapq를 이용해서 가장 작은 값들끼리 더하는 것을 반복하면 326
import sys
import heapq

N = int(input())
Cards = []
C_sum = 0
for _ in range(N) :
    heapq.heappush(Cards,int(sys.stdin.readline().rstrip()))

while len(Cards) - 1 :
    val1 = heapq.heappop(Cards)
    val2 = heapq.heappop(Cards)
    heapq.heappush(Cards,val1+val2)
    C_sum = C_sum + val1 + val2
print(C_sum)

# 틀림
# n개의 카드를 더할 때, (n-1)*(x1+x2)+(n-2)*x3+...+xn 이라는 수식 세워서 해봤는데..
# import sys
#
# N = int(input())
# if N == 1 :
#     Cards_1 = int(sys.stdin.readline().rstrip())
#     print(Cards_1)
# else :
#     Cards = []
#     new_Card = []
#     C_sum = 0
#     for _ in range(N) :
#         Cards.append(int(sys.stdin.readline().rstrip()))
#
#     Cards.sort()
#     new_Card.append(sum(Cards[:2]))
#     new_Card = new_Card + Cards[2:]
#     for i in new_Card :
#         N -= 1
#         C_sum += N*i
#
#     print(C_sum)

#틀림
# import sys

# N = int(input())

# if N == 1 :
#     Cards_1 = int(sys.stdin.readline().rstrip())
#     print(Cards_1)
# else :
#     Cards = []
#     for _ in range(N) :
#         Cards.append(int(sys.stdin.readline().rstrip()))
#     Cards.sort()
#     C_sum = Cards[0]
#     C_sum_list = []
#     for i in Cards[1:] :
#         C_sum = C_sum + i
#         C_sum_list.append(C_sum)
#     print(sum(C_sum_list))