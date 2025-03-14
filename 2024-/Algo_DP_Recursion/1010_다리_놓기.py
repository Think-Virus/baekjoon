import sys


def input_data():
    t = int(sys.stdin.readline())
    test_cases = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

    return test_cases


def solve(test_cases):
    for n, m in test_cases:
        if n == 0 or m == 0:
            print(0)
            continue
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j] = dp[1][j - 1] + 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = sum(dp[i - 1][:j])

        print(dp[n][m])


if __name__ == "__main__":
    test_cases = input_data()
    solve(test_cases)
