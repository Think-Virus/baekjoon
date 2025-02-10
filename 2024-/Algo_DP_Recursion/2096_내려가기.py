"""
문제
    N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다.
    내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.
    먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다.
    그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다.
    바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이
    제약 조건을 그림으로 나타내어 보면 다음과 같다.
    별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며,
    빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다.
    숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오.
    점수는 원룡이가 위치한 곳의 수의 합이다.

입력
    첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다.
    다음 N개의 줄에는 숫자가 세 개씩 주어진다.
    숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

출력
    첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

3
1 2 3
4 5 6
4 9 0
---
접근법
    m[i][j] : 주어진 게임에서 [i][j] 좌표의 값
    dp[i][j] : [i][j]까지 가는 길의 최대값

    max_dp[i][j]:
        max(max_dp[i-1][j], max_dp[i-1][j-1] if j == 2
        max(max_dp[i-1][j], max_dp[i-1][j-1], max_dp[i-1][j+1] if j == 1
        max(max_dp[i-1][j], max_dp[i-1][j+1] if j == 0

    min_dp[i][j]:
        min(min_dp[i-1][j], min_dp[i-1][j-1] if j == 2
        min(min_dp[i-1][j], min_dp[i-1][j-1], max_dp[i-1][j+1] if j == 1
        min(min_dp[i-1][j], min_dp[i-1][j+1] if j == 0
"""
import sys


def solve():
    n = int(sys.stdin.readline())
    max_arr = [int(num) for num in sys.stdin.readline().split()]
    min_arr = max_arr[:]

    max_temp = max_arr[:]
    min_temp = max_arr[:]

    for _ in range(n - 1):
        b1, b2, b3 = map(int, sys.stdin.readline().split())
        max_arr[0] = b1 + max(max_temp[0], max_temp[1])
        max_arr[1] = b2 + max(max_temp[0], max_temp[1], max_temp[2])
        max_arr[2] = b3 + max(max_temp[1], max_temp[2])

        min_arr[0] = b1 + min(min_temp[0], min_temp[1])
        min_arr[1] = b2 + min(min_temp[0], min_temp[1], min_temp[2])
        min_arr[2] = b3 + min(min_temp[1], min_temp[2])

        max_temp = max_arr[:]
        min_temp = min_arr[:]

    print(max(max_arr), min(min_arr))


if __name__ == '__main__':
    solve()
