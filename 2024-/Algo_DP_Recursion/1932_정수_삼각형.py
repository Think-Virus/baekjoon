import sys


def input_data():
    n = int(sys.stdin.readline())
    int_tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    return n, int_tri


def solve(n, int_tri):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = int_tri[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + int_tri[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + int_tri[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + int_tri[i][j]

    print(max(dp[n - 1]))


if __name__ == "__main__":
    n, int_tri = input_data()
    solve(n, int_tri)
