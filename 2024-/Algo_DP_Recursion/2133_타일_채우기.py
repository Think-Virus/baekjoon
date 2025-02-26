"""
문제
    3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
    첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
    첫째 줄에 경우의 수를 출력한다.
"""


def solve():
    n = int(input())
    dp = [0] * (n + 5)
    dp[2] = 3
    dp[4] = 11
    for curr in range(6, n + 1, 2):
        dp[curr] = 2 * dp[curr - 2] * dp[2] + 2 + 2 * 2 * int((n - 6) / 2)
    print(dp[n])


if __name__ == "__main__":
    solve()
