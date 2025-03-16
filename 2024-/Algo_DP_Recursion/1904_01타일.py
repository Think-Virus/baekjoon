def solve():
    n = int(input())
    dp1 = 1
    dp2 = 2
    dp3 = dp1 + dp2

    for i in range(4, n + 1):
        dp1 = dp2
        dp2 = dp3
        dp3 = dp1 + dp2
    print(dp3 % 15746)


if __name__ == '__main__':
    solve()
