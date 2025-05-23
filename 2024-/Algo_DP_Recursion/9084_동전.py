"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	16246	10809	8781	67.593%

문제
    우리나라 화폐단위, 특히 동전에는 1원, 5원, 10원, 50원, 100원, 500원이 있다.
    이 동전들로는 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다.
    예를 들어, 30원을 만들기 위해서는 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능하다.
    동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.

입력
    입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.
    각 테스트 케이스의 첫 번째 줄에는 동전의 가지 수 N(1 ≤ N ≤ 20)이 주어지고 두 번째 줄에는 N가지 동전의 각 금액이 오름차순으로 정렬되어 주어진다.
    각 금액은 정수로서 1원부터 10000원까지 있을 수 있으며 공백으로 구분된다. 세 번째 줄에는 주어진 N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)이 주어진다.
    편의를 위해 방법의 수는 2^31 - 1 보다 작고, 같은 동전이 여러 번 주어지는 경우는 없다.

출력
    각 테스트 케이스에 대해 입력으로 주어지는 N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한 줄에 하나씩 출력한다.

3
2
1 2
1000
3
1 5 10
100
2
5 7
22

1
2
1 3
10
---
1시간 혼자 도전해봄
https://d-cron.tistory.com/23
"""
import sys


def input_data():
    t = int(sys.stdin.readline())
    test_cases = []
    for _ in range(t):
        n = int(sys.stdin.readline())
        coins = [0] + list(map(int, sys.stdin.readline().split()))
        goal = int(sys.stdin.readline())
        test_cases.append([n, coins, goal])

    return test_cases


def solve(test_cases):
    for n, coins, goal in test_cases:
        dp = [[0] * (goal + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(goal + 1):
                curr_coin = coins[i]
                if j - curr_coin >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - curr_coin]
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp[-1][-1])


if __name__ == '__main__':
    test_cases = input_data()
    solve(test_cases)
