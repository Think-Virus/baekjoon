import sys


def input_data():
    t = int(sys.stdin.readline())
    test_cases = []
    for _ in range(t):
        k = int(sys.stdin.readline())
        costs = list(map(int, sys.stdin.readline().split()))

        test_cases.append((k, costs))

    return test_cases


def solve(test_cases):
    INF = float('inf')
    for k, costs in test_cases:
        sub_sum = [[0] * k for _ in range(k)]
        dp = [[INF] * k for _ in range(k)]

        for i in range(k):
            sub_sum[i][i] = costs[i]

        for _j in range(1, k):
            for i in range(k):
                j = i + _j

                if j >= k:
                    break

                ni = i + 1
                nj = i
                sub_sum[i][j] = sub_sum[i][nj] + sub_sum[ni][j]

        for i in range(k):
            dp[i][i] = 0

        for _j in range(1, k):
            for i in range(k):
                j = i + _j

                if j >= k:
                    break

                for g in range(1, _j + 1):
                    ni = i + g
                    nj = i + g - 1
                    dp[i][j] = min(dp[i][nj] + dp[ni][j] + sub_sum[i][j], dp[i][j])

        print(dp[0][k - 1])


if __name__ == "__main__":
    test_cases = input_data()
    solve(test_cases)
