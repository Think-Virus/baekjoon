"""
문제
    3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
    첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
    첫째 줄에 경우의 수를 출력한다.
---
잘못 생각한 부분 이해 완료
https://jyeonnyang2.tistory.com/51
"""


def solve():
    n = int(input())
    dp = [0] * (n + 5)
    dp[2] = 3
    dp[4] = 11
    for curr in range(6, n + 1, 2):
        total = 0
        total += dp[curr - 2] * dp[2]
        for l in range(4, curr + 1, 2):
            total += dp[curr - l] * 2
        dp[curr] = total + 2
    print(dp[n])


if __name__ == "__main__":
    solve()
