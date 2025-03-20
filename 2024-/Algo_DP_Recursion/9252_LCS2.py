def solve():
    first = input()
    second = input()

    dp = [[[0, ''] for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j][0] = dp[i - 1][j - 1][0] + 1
                dp[i][j][1] = dp[i - 1][j - 1][1] + first[i - 1]
            else:
                if dp[i][j - 1][0] > dp[i - 1][j][0]:
                    dp[i][j][0] = dp[i][j - 1][0]
                    dp[i][j][1] = dp[i][j - 1][1]
                else:
                    dp[i][j][0] = dp[i - 1][j][0]
                    dp[i][j][1] = dp[i - 1][j][1]

    result_len, result_str = dp[len(first)][len(second)]
    print(result_len)
    print(result_str)


if __name__ == '__main__':
    solve()
