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

2 1
10
20
"""
import sys


def input_data():
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    for _ in range(n):
        coin = int(sys.stdin.readline())
        if coin <= k:
            coins.append(coin)
    coins.sort()
    return n, k, coins


def solve():
    n, k, coins = input_data()

    def make_dp(n, k, coins):
        # Init
        dp = [10001 for _ in range(k + 1)]
        dp[0] = 0

        for i in range(1, k + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp

    dp = make_dp(n, k, coins)
    print(-1 if dp[k] == 10001 else dp[k])


if __name__ == '__main__':
    solve()
