"""
문제
    수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
    예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
    첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
    둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
    첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
    둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

6
10 20 10 30 20 50

PyPy로 시도
"""


def input_data():
    n = int(input())
    nums = list(map(int, input().split()))

    return n, nums


def solve(n, nums):
    dp = [[0] * n for _ in range(n)]
    dp_nums_dict = {}

    for i in range(n):
        dp[i][i] = 1
        dp_nums_dict[i] = [nums[i]]

    """
    1 2     1 3
    2 3     2 4
    3 4     3 5
    """
    for _j in range(1, n):
        for i in range(n):
            j = i + _j
            if j > n - 1:
                continue

            if nums[i] < nums[j]:
                max_len = 0
                max_len_idx = 0
                for k in range(_j):
                    next_idx = i + 1 + k
                    if next_idx > n - 1:
                        break
                    if nums[i] < nums[next_idx]:
                        if max_len < dp[next_idx][j]:
                            max_len = dp[next_idx][j]
                            max_len_idx = next_idx
                if not max_len:
                    dp[i][j] += 1
                    dp_nums_dict[i].append(nums[j])
                else:
                    dp[i][j] = max_len + 1
                    dp_nums_dict[i] = [nums[i]] + dp_nums_dict[max_len_idx]
            else:
                dp[i][j] = dp[i][j - 1]

    max_len = 0
    max_len_idx = 0
    for i in range(n):
        if max_len < dp[i][n - 1]:
            max_len = dp[i][n - 1]
            max_len_idx = i

    print(max_len)
    print(*dp_nums_dict[max_len_idx])


if __name__ == '__main__':
    n, nums = input_data()
    solve(n, nums)
