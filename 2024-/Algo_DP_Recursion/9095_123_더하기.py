"""문제
    정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
    1+1+1+1
    1+1+2
    1+2+1
    2+1+1
    2+2
    1+3
    3+1
    정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
    각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
---
1시간 고민했으나 각이 안 나옴
---
내가 계산했던 게 맞기는 한 것 같은데, 원리는 잘 모르겠음 -> 규칙을 찾은 느낌
dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
각각 마지막 숫자를 의미한다고 생각하면 됨
    - 마지막 숫자가 1이고 i-1 숫자를 만드는 개수
    - 마지막 숫자가 2이고 i-2 숫자를 만드는 개수
    - 마지막 숫자가 3이고 i-3 숫자를 만드는 개수

ex)
    1 : 1
    2 : 1 1 / 2
    3 : 1 1 1 / 1 2 / 2 1 / 3
    4 :
        - 1로 끝나는 경우 -> 4-1 = dp[3]
            1 1 1 1
            1 2 1
            2 1 1 1
            3 1
        - 2로 끝나는 경우 -> 4-2 = dp[2]
            1 1 2
            2 2
        - 3로 끝나는 경우 -> 4-3 = dp[3]
            1 3
"""
import sys


def input_data():
    t = int(sys.stdin.readline())
    test_data = [int(sys.stdin.readline()) for _ in range(t)]

    return test_data


def solve(test_data):
    dp = []
    last_idx = 3
    for n in test_data:
        if n < 4:
            if n == 1:
                print(1)
            elif n == 2:
                print(2)
            else:
                print(4)
            continue

        # Init
        if not dp:
            dp = [0] * max(test_data)
            dp[0] = 1
            dp[1] = 2
            dp[2] = 4

        if last_idx >= n:
            # computed Already
            print(dp[n - 1])
        else:
            # need to compute
            for i in range(last_idx, n):
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            last_idx = n
            print(dp[n - 1])


if __name__ == '__main__':
    test_data = input_data()
    solve(test_data)
