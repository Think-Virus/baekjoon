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
---
정답 접근법
    LIS (Longest Increasing Subsequence) 배열 생성
        dp_incr[i]: i 번째 원소까지 고려했을 때 증가하는 가장 긴 부분 수열 길이
    LDS (Longest Decreasing Subsequence) 배열 생성
        dp_decr[i]: i 번째 원소부터 시작했을 때 감소하는 가장 긴 부분 수열 길이
    최댓값 찾기
        dp_incr[i] + dp_decr[i] - 1 중 최댓값을 찾기
"""
import sys


def input_data() -> (int, list[int]):
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))

    return n, seq


def solve():
    n, seq = input_data()

    def longest_bitonic_subsequence(n, seq):
        # 1. LIS 배열 (Increasing Subsequence)
        dp_incr = [1] * n
        for i in range(n):
            for j in range(i):
                if seq[j] < seq[i]:
                    dp_incr[i] = max(dp_incr[i], dp_incr[j] + 1)

        # 2. LDS 배열 (Decreasing Subsequence)
        dp_decr = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if seq[j] < seq[i]:
                    dp_decr[i] = max(dp_decr[i], dp_decr[j] + 1)

        # 3. 가장 긴 바이토닉 수열 길이 찾기
        max_length = 0
        for i in range(n):
            max_length = max(max_length, dp_incr[i] + dp_decr[i] - 1)

        return max_length

    max_length = longest_bitonic_subsequence(n, seq)
    print(max_length)


if __name__ == '__main__':
    solve()
