"""
문제
    n개의 정수로 이루어진 임의의 수열이 주어진다.
    우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
    단, 수는 한 개 이상 선택해야 한다.
    예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
    여기서 정답은 12+21인 33이 정답이 된다.

입력
    첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
    수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
    첫째 줄에 답을 출력한다.

10
2 1 -4 3 4 -4 6 5 -5 1
"""


def input_data():
    n = int(input())
    numbers = list(map(int, input().split()))

    return n, numbers


def solve(n, numbers):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = numbers[i]

    for i in range(n - 2, -1, -1):
        for j in range(1, n - i):
            k = i + j
            dp[i][k] = max(dp[i][k - 1], dp[i][i] + dp[i + 1][k])

    max_sum = dp[-1][-1]
    for i in range(n):
        max_sum = max(max_sum, dp[i][-1])

    print(max_sum)


if __name__ == '__main__':
    n, numbers = input_data()
    solve(n, numbers)
