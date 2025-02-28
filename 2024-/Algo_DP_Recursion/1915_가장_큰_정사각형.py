"""
문제
    n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.
    0	1	0	0
    0	1	1	1
    1	1	1	0
    0	0	1	0
    위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.

입력
    첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

출력
    첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.
"""
import sys


def input_data():
    n, m = map(int, sys.stdin.readline().split())
    arrays = [[0] * (n + 1)] + [[0] + list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(m)]

    return n, m, arrays


def solve(n, m, arrays):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_size = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arrays[i][j] == 1:
                if dp[i][j - 1] != 0 and dp[i - 1][j - 1] != 0 and dp[i - 1][j] != 0:
                    l = min((dp[i - 1][j]), dp[i - 1][j - 1], dp[i][j - 1]) ** 0.5
                    dp[i][j] = 3 * l ** 2 + 1 - (2 * (l - 1) ** 2 + 2 * (l - 1))
                else:
                    dp[i][j] = 1

                max_size = max(max_size, dp[i][j])

    print(int(max_size))


if __name__ == '__main__':
    n, m, arrays = input_data()
    solve(n, m, arrays)
