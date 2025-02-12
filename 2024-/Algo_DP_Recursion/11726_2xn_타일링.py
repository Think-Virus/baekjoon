"""
문제
    2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
    아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
    첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
    첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
---
접근법
    1) 5까지 해본 결과, dp[n] = dp[n-1] + dp[n-2]
"""


def solve():
    n = int(input())

    def make_dp(n):
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            if i == 2:
                dp[2] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp

    dp = make_dp(n)
    print(dp[n] % 10007)


if __name__ == '__main__':
    solve()
