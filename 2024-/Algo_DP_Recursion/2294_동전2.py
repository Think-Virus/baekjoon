"""
문제
    n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서,
    그 가치의 합이 k원이 되도록 하고 싶다.
    그러면서 동전의 개수가 최소가 되도록 하려고 한다.
    각각의 동전은 몇 개라도 사용할 수 있다.

입력
    첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
    다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
    동전의 가치는 100,000보다 작거나 같은 자연수이다.
    가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
    첫째 줄에 사용한 동전의 최소 개수를 출력한다.
    불가능한 경우에는 -1을 출력한다.

3 15
1
5
12

3 15
2
5
12

1 10
1
"""
import sys


def input_data():
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coin = int(sys.stdin.readline())
        if coin <= k:
            coins.append(coin)
    return n, k, coins


def solve():
    n, k, coins = input_data()

    def make_dp(n, k, coins):
        # Init
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]
        for coin in coins:
            dp[coin] = [1 for _ in range(n)]

        for i in range(k + 1):
            for j, coin in enumerate(coins):
                if i - coin < 0:
                    continue
                else:
                    is_prev = False
                    prev_value = i - coin
                    prev_min_count = 0
                    for t in range(n):
                        if dp[prev_value][t]:
                            is_prev = True
                            if prev_min_count:
                                prev_min_count = min(prev_min_count, dp[prev_value][t])
                            else:
                                prev_min_count = dp[prev_value][t]
                    if is_prev:
                        dp[i][j] = prev_min_count + 1
        return dp

    dp = make_dp(n, k, coins)
    min_count = 0
    for c in dp[k]:
        if c:
            if not min_count:
                min_count = c
            else:
                min_count = min(min_count, c)
    if not min_count:
        min_count = -1

    print(min_count)


if __name__ == '__main__':
    solve()
