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
---
접근 방식
1. 물건을 선택하거나 선택하지 않을 때의 최적값을 계산함
2. DP 테이블을 정의하고, 작은 문제를 통해 큰 문제를 해결함
---
DP 테이블 정의
- dp[j]를 배낭의 무게 한도가 j일 때 얻을 수 있는 최대 가치로 정의
- dp 배열의 크기는 K+1 (무게 한도는 0~K까지)
---
점화식
1. 현재 물건을 넣지 않았을 때: dp[j]는 변하지 않음
2. 현재 물건을 넣을 때: 무게가 W이고, 가치가 V인 현재 물건에 대해,
    dp[j] = max(dp[j], dp[j-W] + V)
"""
import sys

N, K = map(int, sys.stdin.readline().split())
wv_list: list[list[int]] = list([list(map(int, sys.stdin.readline().split())) for _ in range(N)])


def knapsack(wv_list: list[list[int]], K) -> int:
    dp = [0] * (K + 1)
    for w, v in wv_list:
        # print(f"{K} ~ {w-1}")
        for j in range(K, w - 1, -1):
            # print(f"w: {w} / v: {v} / dp[{j}]: {dp[j]}")
            # print(dp)
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[K]


print(knapsack(wv_list, K))
