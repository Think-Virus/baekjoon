"""
문제
    수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면,
    그 수열을 바이토닉 수열이라고 한다.
    예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
    {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
    수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다.
    (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
    첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

10
1 5 2 1 4 3 4 5 2 1

7

6
5 1 6 2 3 1

4
---
접근법
    seq[i] : 수열의 i번째 값
    dp[i][j] : [biggest_length, state]
        biggest_length : seq[i]로 시작하는 바이토닉 수열 중 j번째까지 확인했을 때, 가장 긴 바이토닉 수열의 길이
        state :
            0 : 증가하는 수열 -> seq[i]가 seq[t]보다 작으면, 앞에 붙이고 state = 0, 아닌 건 불가능
            1 : 감소하는 수열 -> 그냥 앞에 붙일 수 있으며, 만약 seq[i]가 seq[t]보다 크면 state = 1, 작으면 state = 2
            2 : 증가하다가 감소한 수열 -> seq[i]가 seq[t]보다 작으면, 앞에 붙이고 state = 2, 아닌 건 불가능

    처음 초기화
        dp[1][1] = dp[2][2] = ... = dp[n][n] = 1
        dp[1][2] = ... = dp[n][n+1] = 2
            2를 설정하면서 상태 설정
            이 과정에서 같은 값일 경우 이어지는 데 문제가 발생함
            연속해서 같은 값이 있는 경우는 제거하고 가는 게 좋을듯
"""
import sys

TYPE_INCREASING = 0
TYPE_DECREASING = 1
TYPE_CURVED = 2


def input_data() -> (int, list[int]):
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))

    # clean sequence : sequentially duplicated number delete
    n = 0
    pre_num = 0
    cleaned_seq = []
    for num in seq:
        if num != pre_num:
            cleaned_seq.append(num)
            n += 1
        pre_num = num

    return n, cleaned_seq


def solve():
    n, seq = input_data()

    def make_dp(n, seq) -> list[list[list[int]]]:
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i][0] = 1

            if i == n - 1:
                break

            if seq[i] > seq[i + 1]:
                dp[i][i + 1] = [2, TYPE_DECREASING]
            elif seq[i] < seq[i + 1]:
                dp[i][i + 1] = [2, TYPE_INCREASING]

        for k in range(2, n):
            for i in range(n):
                j = i + k
                if j == n:
                    break

                max_len = [dp[i][j - 1][0], dp[i][j - 1][1]]
                for t in range(1, j - i + 1):
                    cur_len = dp[i + t][j][0]
                    cur_type = dp[i + t][j][1]

                    if cur_len < max_len[0]:
                        continue

                    if seq[i] > seq[i + t]:
                        if cur_type == TYPE_DECREASING:
                            max_len = [cur_len + 1, TYPE_DECREASING]
                    elif seq[i] < seq[i + t]:
                        max_len[0] = cur_len + 1
                        if cur_type == TYPE_DECREASING:
                            max_len[1] = TYPE_CURVED
                        elif cur_type == TYPE_INCREASING:
                            max_len[1] = TYPE_INCREASING
                        else:
                            max_len[1] = TYPE_CURVED

                dp[i][j] = max_len

        return dp

    dp = make_dp(n, seq)

    max_len = 0
    for i in range(n):
        if dp[i][n - 1][0] > max_len:
            max_len = dp[i][n - 1][0]
    print(max_len)


if __name__ == '__main__':
    solve()
