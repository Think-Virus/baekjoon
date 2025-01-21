"""
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
---
접근법
    lcs[i,j] : 두 수열 s1[0:i], s2[0:j]의 최장 공통 수열의 크기
    lcs[i,j] =
        lcs[i-1, j-1] + 1 if s1[i] == s2[j]
        max(lcs[i-1,j], lcs[i, j-1] else
"""
import sys


def input_data():
    s1 = list(sys.stdin.readline().rstrip())
    s2 = list(sys.stdin.readline().rstrip())

    return s1, s2


def solve():
    s1, s2 = input_data()

    def make_dp(s1, s2) -> list[list[int]]:
        dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if s2[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp

    dp = make_dp(s1, s2)

    print(dp[len(s2)][len(s1)])


if __name__ == '__main__':
    solve()
