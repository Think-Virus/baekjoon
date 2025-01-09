"""
이 문제는 아주 평범한 배낭에 관한 문제이다.
한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이다.

한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

4 7
6 13
4 8
3 6
5 12

"""
import copy
import sys

N, K = map(int, sys.stdin.readline().split())
WV_list = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda wv: wv[1] / wv[0], reverse=True)

"""
새롭게 배운 점
data = [list(map(lambda wv: [wv[0], wv[1], wv[1] / wv[0]], list(map(int, sys.stdin.readline().split())))) for _ in range(N)]
이렇게 했었을 때, ValueError: invalid literal for int() with base 10: 'import' 에러 발생
이유? -> wv 값이 6으로 들어갔기 때문에 [6, 13]
왜 그랬을까? lambda를 적용핼 때, map으로 해서 list를 순환하는 식으로 했기에 6으로 되는 게 정상 동작이었음.
어떻게 해결? -> lambda를 직접 적용하는 식으로 변경함!
"""

def select_item(WV_list: list, curr_weight=0, curr_sum=0):
    # Confirm current limit and next action
    curr_limit = K - curr_weight
    # is_small = any(w <= curr_limit for w in (wv[0] for wv in WV_list))
    # is_small = any(wv[0] <= curr_limit for wv in WV_list)

    # Algorithm
    # 1. If smaller weight item exists in left list, make a new result value.
    # 2. Else if sum of values in the left list is bigger than current result.
    while WV_list:
        for wv in WV_list:
            if wv[0] <= curr_limit:
                print(wv)
                curr_sum += wv[1]
                curr_weight += wv[0]
                WV_list.remove(wv)
                select_item(WV_list, curr_weight, curr_sum)
                break

        if curr_sum < sum([wv[1] for wv in WV_list]):
            prev_curr_sum = curr_sum
            curr_weight = 0
            curr_sum = 0


    return curr_sum

print(select_item(copy.deepcopy(WV_list)))

print(WV_list)
