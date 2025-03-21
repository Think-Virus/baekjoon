import sys


def input_data():
    n = int(sys.stdin.readline())
    matrixs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    return n, matrixs


def solve(n, matrixs):
    INF = float('inf')
    dp = [[INF] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for _j in range(1, n):
        for i in range(n):
            j = i + _j
            if j >= n:
                break
            for k in range(1, _j + 1):
                dp[i][j] = min(dp[i][j], dp[i][i + k - 1] + dp[i + k][j] + matrixs[i][0] * matrixs[j][1] * matrixs[i + k][0])

    print(dp[0][n - 1])


if __name__ == '__main__':
    n, matrix = input_data()
    solve(n, matrix)
