def solve():
    n = int(input())
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[1] = [0, 1]

    for i in range(2, n + 1):
        zero, one = dp[i - 1]
        dp[i] = [one + zero, zero]

    print(sum(dp[n]))


if __name__ == '__main__':
    solve()
