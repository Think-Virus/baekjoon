import sys


def input_data():
    n = int(sys.stdin.readline())
    matrixs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    return n, matrixs


def solve(n, matrixs):
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 2, -1, -1):
        for _j in range(1, n - i):
            j = i + _j
            s_i, e_i = matrixs[i]
            s_j, e_j = matrixs[j]
            if _j == 1:
                dp[i][j] = s_i * s_j * e_j
            else:
                dp[i][j] = min(dp[i][j - 1] + s_i * s_j * e_j, dp[i + 1][j] + s_i * matrixs[i + 1][0] * e_j)

    print(dp[0][n - 1])


if __name__ == '__main__':
    n, matrix = input_data()
    solve(n, matrix)
