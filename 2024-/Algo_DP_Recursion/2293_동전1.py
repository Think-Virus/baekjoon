"""
문제
    n가지 종류의 동전이 있다.
    각각의 동전이 나타내는 가치는 다르다.
    이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
    그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
    사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
    첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
    다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
    동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
    첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.
---
접근법
    coin in coins:
        dp[i] = dp[i-coin] + 1
        모르겠음 -> 고민 시간 : 30분
"""
import sys


def input_data() -> (int, list[int]):
    n, k = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    coins.sort()
    return k, coins


def solve():
    k, coins = input_data()

    def make_dp(k, coins):
        dp = [0 for _ in range(k + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, k + 1):
                dp[i] += dp[i - coin]
        return dp

    dp = make_dp(k, coins)
    print(dp[k])


if __name__ == '__main__':
    solve()
