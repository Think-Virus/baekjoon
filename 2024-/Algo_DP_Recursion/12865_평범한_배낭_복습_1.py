"""
입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

4 7
6 13
4 8
3 6
5 12

14
"""
import sys


def knapsack(K: int, items: list[list[int]]) -> int:
    dp = [0] * (K + 1)

    for w, v in items:
        for j in range(K, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[K]


def main():
    N, K = map(int, input().split())
    items: list[list[int]] = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(knapsack(K, items))


if __name__ == "__main__":
    main()
