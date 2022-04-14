# N개의 숫자 구슬이 <그림 1>과 같이 막대에 꿰어져 일자로 놓여 있다. 이들 구슬은 막대에서 빼낼 수 없고, 바꿀 수 없다.

# 이 숫자 구슬을 M개의 그룹으로 나누었을 때 각각의 그룹의 합 중 최댓값이 최소가 되도록 하려 하다.
# 예를 들어 세 그룹으로 나눈다고 할 때 <그림 2>와 같이 그룹을 나누면 그룹의 합은 각각 11, 15, 18이 되어 그 중 최댓값은 18이 되고,
# <그림 3>과 같이 나누면 각 그룹의 합은 각각 17, 12, 15가 되어 그 중 최댓값은 17이 된다.
# 숫자 구슬의 배열이 위와 같을 때는 그룹의 합 중 최댓값이 17보다 작게 만들 수는 없다.
# 그룹에 포함된 숫자 구슬의 개수는 0보다 커야 한다.

# 그룹의 합 중 최댓값이 최소가 되도록 M개의 그룹으로 나누었을 때,
# 그 최댓값과 각 그룹을 구성하는 구슬의 개수를 찾아 출력하는 프로그램을 작성하시오.

# 입력 :
# 첫째 줄에 쪽부터 차례로 주어진다구슬의 개수 N과 그룹의 수 M이 주어진다.
# # 둘째 줄에는 각 구슬이 적혀진 숫자가 왼. N은 300 이하의 자연수, M은 N이하의 자연수이며,
# 구슬에 적혀진 숫자는 100 이하의 자연수이다.

# 출력 :
# 각 그룹의 합 중 최댓값이 최소가 되도록 M개의 그룹으로 나누었을 때 그 최댓값을 첫째 줄에 출력하고,
# 둘째 줄에는 각 그룹을 구성하는 구슬의 개수를 왼쪽부터 순서대로 출력한다. 구슬의 개수를 출력할 때는 사이에 한 칸의 공백을 둔다.
# 만약 그룹의 합의 최댓값이 최소가 되도록 하는 경우가 둘 이상이라면 그 중 하나만을 출력한다.

"""
In :
8 3
5 4 2 6 9 3 8 7

Out :
17
4 2 2
"""
from collections import deque
N,M = map(int,input().split())
marble_list = deque(map(int,input().split()))
deque_list = []
for _ in range(M-1) :
    deque_list.append(deque([marble_list.popleft()]))
deque_list.append(marble_list)

pre_max_val = 100**300+2
max_val = 100**300+1

while pre_max_val >= max_val :
    # 가장 큰 그룹부터 확인
    pre_max_val = max_val
    tmp_list = list(map(sum, deque_list))
    min_idx = tmp_list.index(min(tmp_list)) # 가장 값이 작은 그룹
    if min_idx != len(tmp_list)-1 : # 최소값이 마지막이 아닐 때
        deque_list[min_idx].append(deque_list[min_idx+1].popleft())
    else : # 마지막일 때
        deque_list[min_idx].appendleft(deque_list[min_idx - 1].pop())
    max_val = max(map(sum,deque_list))

if not pre_max_val >= max_val :
    deque_list[min_idx+1].appendleft(deque_list[min_idx].pop())
print(max(map(sum,deque_list)))
for i in map(len,deque_list) :
    print(i, end=' ')




