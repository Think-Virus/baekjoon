def solve():
    first = input()
    second = input()

    dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

    result_str = ""
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > len(result_str):
                    result_str += first[i - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    print(dp[len(first)][len(second)])
    print(result_str)


if __name__ == '__main__':
    solve()
