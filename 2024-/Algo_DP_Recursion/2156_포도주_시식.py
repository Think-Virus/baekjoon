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
"""
import sys


class OrderType:
    def __init__(self, order_type: int):
        self.type: int = order_type
        self.prev_types: list[int] = []

        # init
        self.init_prev_types()

    def init_prev_types(self):
        if self.type == 1:
            self.prev_types = [3, 4]
        elif self.type == 2:
            self.prev_types = [1, 3]
        elif self.type == 3:
            self.prev_types = [2, 4]
        else:
            self.prev_types = [1, 2]


def input_data() -> (int, list[int]):
    n = int(sys.stdin.readline())
    wines = [int(sys.stdin.readline()) for _ in range(n)]
    return n, wines


def make_dp(n, wines):
    dp = [[0] * (n + 1) for _ in range(5)]
    types = [OrderType(1), OrderType(2), OrderType(3), OrderType(4)]
    wines.insert(0, 0)

    # Init index 1 in dp
    for i in range(3, 5):
        dp[i][1] = wines[1]

    for i in range(2, n + 1):
        for p in types:
            prev_max = 0
            for prev_p in p.prev_types:
                prev_max = max(prev_max, dp[prev_p][i - 2])
            if p.type == 1:
                dp[1][i] = prev_max
            elif p.type == 2:
                dp[2][i] = prev_max + wines[i - 1]
            elif p.type == 3:
                dp[3][i] = prev_max + wines[i]
            else:
                dp[4][i] = prev_max + wines[i] + wines[i - 1]

    max_wine = 0
    for i in range(1,5):
        max_wine = max(max_wine, dp[i][n])
    print(max_wine)

def solve():
    n, wines = input_data()
    make_dp(n, wines)


if __name__ == "__main__":
    solve()
