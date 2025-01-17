"""
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
---
접근법
    dp 테이블 구성 :
        - N번째 자리의 값이 i(0~9)인 숫자들은 N-1번째 자리 값 중 i-1과 i+1의 값들의 개수의 합으로 결정됨
        - dp[i][1] = [1,1,2,2,2,2,2,2,2,1]
        - dp[i][N] = dp[i-1][N-1] + dp[i+1][N-1] if N > 1
"""


def solve():
    n = int(input())

    # for debug
    def print_dp(dp):
        for i in range(12):
            print(f"{i - 1}: {dp[i]}")

    def idx(i):
        # The real indexes are 0 ~ 10, but I want to use 0 ~ 9 to identify easy.
        return i + 1

    def make_dp(n) -> list[list[int]]:
        # Init dp
        dp = [[0] * (n + 1) for _ in range(12)]
        for i in range(1, 10):
            dp[idx(i)][1] = 1

        for i in range(2, n + 1):
            for j in range(1, 11):
                dp[j][i] = dp[j - 1][i - 1] + dp[j + 1][i - 1]

        return dp

    def get_result(dp) -> int:
        result = 0
        for i in range(12):
            result += dp[i][n]
        return result % 1000000000

    dp = make_dp(n)
    print(get_result(dp))


if __name__ == '__main__':
    solve()
