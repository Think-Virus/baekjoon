"""
문제
효주는 포도주 시식회에 갔다. 그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다. 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오.

예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

입력
첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

6
6
10
13
9
8
1
---
접근법
    dp[N] : N잔을 마실 때, 최대 와인의 양
    wine[i] : i번째 순서에 있는 와인의 양
    dp[0] = 0
    dp[1] = w[1]
    dp[2] = w[1] + w[2]
    dp[3] = max(w[1] + w[2], w[2] + w[3], w[1] + w[3])
    dp[N]의 경우
        1. N번째에 마신다면?
            (1) N-1번째에 마시는 경우
                N-3 : 여기까지 마심
                N-2 : 못마심
                N-1 :마심
                N : 마심
                -> dp[N] = w[N] + w[N-1] + dp[N-3]
            (2) N-1번째에 마시지 않는 경우
                N-2 : 마심
                N-1 :안마심
                N : 마심
                -> dp[N] = w[N] + dp[N-2]
        2. N번째에 마시지 않는다면
            N-1 : 마심
            N : 안마심
            -> dp[N] = dp[N-1]
"""
import sys


def input_data() -> (int, list[int]):
    n = int(sys.stdin.readline())
    wines = [int(sys.stdin.readline()) for _ in range(n)]
    wines.insert(0, 0)
    return n, wines


def make_dp(n, wines) -> int:
    dp = [0] * (n + 1)
    if n == 1:
        return wines[1]
    elif n == 2:
        return wines[2] + wines[1]

    dp[1] = wines[1]
    dp[2] = wines[1] + wines[2]
    dp[3] = max(wines[1] + wines[2], wines[2] + wines[3], wines[1] + wines[3])
    if n == 3:
        return dp[3]

    for i in range(4, n + 1):
        dp[i] = max(
            wines[i] + wines[i - 1] + dp[i - 3],
            wines[i] + dp[i - 2],
            dp[i - 1]
        )

    return dp[n]

def solve():
    n, wines = input_data()
    maximum_wine = make_dp(n, wines)
    print(maximum_wine)


if __name__ == '__main__':
    solve()
